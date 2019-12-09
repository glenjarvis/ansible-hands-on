#!/usr/bin/python

# Copyright: (c) 2018-2020, Glen Jarvis Training & Consulting, LLC
# <glen@glenjarvis.com>
# MIT License:
# https://github.com/glenjarvis/ansible_hands_on_training/blob/develop/LICENSE


ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: process_monitor

short_description: >
    Example custom module that returns Process Show (ps) data

version_added: "2.4"

description: >
    An example custom module for the Ansible Hands On Training course.
    This module returns Process Show (ps) data in structured format so
    that this process information could be exposed to a playbook.
    The need for this module taken from a Stack Overflow example where
    users were using `script` instead of a custom module
    https://stackoverflow.com/questions/20563639/ansible-playbook-shell-output.

options:
    user_defined_fields:
        description: The paramers to monitor
        required: false
        default: 'pcpu,user,args'
        version_added: 0.0
    sort_key:
        description: The ps output column header to use for sorting
        required: false
        default: '%CPU'
        version_added: 0.0
    reverse:
        description: Boolean flag for direction of sorted results
        required: false
        default: 'true'
        version_added: 0.0
    field_length:
        description: Maximum length of field data (on supported OS)
        required: false
        default: 120
        version_added: 0.0
    number_of_results:
        description: How many results to return
        required: false
        default: 5
        version_added: 0.0

author:
    - Glen Jarvis (@glenjarvis)
'''

EXAMPLES = '''
#  Note that the results, by their very nature, will vary. This module
#  does not make any system changes (to keep idempotence). However,
#  relying on the results (e.g., conditional behavior on results) will
#  break idempotence and be flaky at best.

# Default usage:
- hosts: demoserver
  tasks:
    - process_monitor:

    - name: Demo of all of the results
      debug: var=monit

    - name: Demo how to fetch the most active process
      debug: var=monit['processes'][0]

# Specifying fields:
- hosts: demoserver
  tasks:
    - process_monitor:
        user_defined_fields: pcpu,user,args
        sort_key: "%CPU"
        number_of_results: 3
        reverse: True
      register: monit

    - name: Demo of all of the results
      debug: var=monit

    - name: Demo how to fetch the most active process
      debug: var=monit['processes'][0]

    - debug: var=monit['processes'][0]['USER']

# Lowest amount of CPU
- hosts: demoserver
  tasks:
    - process_monitor:
        user_defined_fields: pcpu,user,args
        sort_key: "%CPU"
        number_of_results: 3
        reverse: False
      register: monit

    - name: Demo of all of the results
      debug: var=monit

    - name: Demo how to fetch the most active process
      debug: var=monit['processes'][0]

    - debug: var=monit['processes'][0]['USER']

#  For operating systems that cannot support fixed length args
#  (e.g., OSX), full structured data can't be reliably created.
#  Therefore, only the first column is split (assuming no spaces). In
#  this case, you should make the sort key the first field.
- hosts: localhost
  tasks:
    - process_monitor:
        user_defined_fields: pcpu,user,args
        sort_key: "%CPU"
        number_of_results: 2
      register: monit

    - name: Demo of all of the results
      debug: var=monit


Sample Results:
TASK [Demo of all of the results] **************************************
ok: [localhost] => {
    "monit": {
        "changed": false,
        "failed": false,
        "message": [],
        "processes": [
            {
                "%CPU": "7.7",
                "USER ARGS": "someuser /Users/... playbook_0300.yml"
            },
            {
                "%CPU": "42.3",
                "USER ARGS": "someuser /Users/..._process_monitor.py"
            }
        ]
    }
}
'''

RETURN = '''
processes:
    description: Collected Process information
    type: dict
    returned: always
'''

from subprocess import Popen, PIPE

from ansible.module_utils.basic import AnsibleModule


def unformatted_fields(output):
    """Given output line, return tuple

    Lines:
    "%CPU USER  COMMAND"
    "0.0  root  /sbin/init"

    Output
     ("%CPU", "USER COMMAND")
     ("0.0", "root  /sbin/init")
    """
    output = output.rstrip()  # We need spacing; don't strip from left
    rows = []
    for line in output.split('\n'):
        line = line.split()
        rows.append(list([line[0].strip(), " ".join(line[1:]).strip()]))
    return rows


def field_length_fields(module):
    """pcpu:30,user:30,args:30"""
    fields = module.params['user_defined_fields'].split(',')
    length = module.params['field_length']
    return ",".join(["%s:%s" % (field, length) for field in fields])


def fixed_length_fields(module, output):
    """Parse output string lists(rows) of lists(cols) by fixed length

    Output will be a large string with embedded new line characters.
    Each line will have a fixed set of fields of a certain length as
    specified by `module.params['field_length']`

    Results will be a list of lists such as:

    [['%CPU', 'USER', 'COMMAND'], ['0.0', 'root', '/sbin/init'], ...]
    """

    length = module.params['field_length']
    output = output.rstrip()  # We need spacing; don't strip from left
    rows = []
    for line in output.split('\n'):
        fields = []
        while line:
            fields.append(line[:length].strip())
            line = line[length:]
        rows.append(list(fields))
    return rows


def ps_collate(module, ps_data, result):
    """Collate PS output data

    Given Process Show data (ps_data), collate results according to
    module.parameters.

    These module parameters affect the results returned:

      * module.params['sort_key']: (e.g, "%CPU")
      * module.params['reverse']: Boolean to reverse sort (e.g., True)
      * module.params['number_of_results']: How many results to return

    Note: `result` is passed into function so more data is available in
          output if a module.exit_json is requred.
    """
    headers = ps_data.pop(0)
    ps_data = [dict(zip(headers, row)) for row in ps_data if row]

    if module.params['sort_key'] in headers:
        ps_data = sorted(ps_data,
                         key=lambda k: k[module.params['sort_key']],
                         reverse=module.params['reverse'])
        ps_data = ps_data[:module.params['number_of_results']]
    else:
        module.fail_json(msg='Sort key %s is not in ps headers: %s' % (
            module.params['sort_key'], headers))
        module.exit_json(**result)

    return ps_data


def _ps(field_string):
    """Execute ps -eo <field_string>

    Returns 3-member: tuple:
      p: Popen process (for return code checking)
      output: Output of command (stdout)
      error: Error output of command (stderr)
    """
    process = Popen(['ps', '-eo', field_string],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE,
                    bufsize=-1)
    output, error = process.communicate()

    return (process, output.decode("utf-8"), error.decode("utf-8"))


def ps(module, result):
    """Fetch a process list

    Given a string which represents what metrics to measure (e.g.,
    pcpu,user,args), fetch those metrics.

    The given module will have params that affect the results given:
      * module.params['user_defined_fields']:(e.g, "pcpu,user,args")

    If the remote operating system supports it, the user defined metrics
    are modified to be of fixed length (e.g., pcpu:30,user:30,args:30).
    This way results can be interpreted and returned as structured data.
    Simply splitting on spaces will be be sufficient as some results
    include embedded spaces. For example, here is an example COMMAND
    field: "sshd: ec2-user@pts/1"

    Notes:
      * Only comma separated metrics are supported (e.g.:
        "pcpu,user,args" not "pcpu user args").
      * These results are further processed in ps_collate
      * Other module.params affect output (see also ps_collate)
    """

    long_fields = field_length_fields(module)
    regular_fields = module.params['user_defined_fields']
    ps_data = []

    process, output, error = _ps(long_fields)
    if process.returncode == 0:
        ps_data = fixed_length_fields(module, output)
    else:
        process, output, error = _ps(regular_fields)
        if process.returncode == 0:
            ps_data = unformatted_fields(output)
        else:
            module.fail_json(msg="PS Error: %s" % error)
            module.exit_json(**result)

    return ps_collate(module, ps_data, result)


def run_module():
    """Ansible module"""
    module_args = dict(
        user_defined_fields=dict(
            type='str', required=False, default='pcpu,user,args'),
        field_length=dict(type='int', required=False, default=120),
        number_of_results=dict(type='int', required=False, default=5),
        sort_key=dict(type='str', required=False, default="%CPU"),
        reverse=dict(type='bool', required=False, default=True),
    )

    result = dict(
        changed=False,
        message=[],
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if not module.check_mode:
        ps_output = ps(module, result)
        # PS never really changes the target:
        result['processes'] = ps_output

    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
