python3_6
=========

The playbook in our teaching example does not rely on an Operating System
version of Python. Instead, we create a virtual Python environment in a
variable specified location.

Once this Python virtualenv is installed, it can be used (loosly coupled) with
other playbooks that require the Python executable.

Note that this is a teaching exercise in Ansible roles. As the student
advances, they may see that this is better done with a custom module instead of
an Ansible role.

Requirements
------------

This role was created as an exercise in a training program. Although we could
dynamically handle different packaging tools, at this stage in the learner's
path, we keep it simple to only using the "yum" package manager.

Therefore, this should be an Amazon Linux, RedHat, Centos, or other
distribution that can install the *python36-libs.x86_64* package via YUM. In
the learner's future path, we will see how to make this more dynamic and fetch
the packages and installation method via operating system.

Role Variables
--------------

The following two default variables are used. Please note that
`python_virtualenv_root` variable is a directory of the root path and not the
final virtualenv destination:

Defaults:
python_virtualenv_root: /local/pythonvenv
python_virtualenv_owner: web

In addition, the following variables re derived from the above defaults:

Vars:
python_virtualenv_dir: "{{ python_virtualenv_root }}/venv"
python_virutalenv_bashrc: /home/{{ python_virtualenv_owner }}/.bashrc

If the `python_virtualenv_dir` is overridden, please ensure that it's root path
exists and is owned by the `python_virtualenv_owner`. It is better not to
override this variable and to override the `python_virtualenv_root` and
`python_virtualenv_owner` variables instead.  Then, this check is done for you.

Dependencies
------------

None

Example Playbook
----------------

    - hosts: webservers
      vars:
        - username: web
      roles:
        - role: non_priviledged_user
          non_priviledged_user_name: "{{ username }}"
          non_priviledged_user_uid: 1100
        - role: python3_6
          python_virtualenv_root: /local/pythonvenv
          python_virtualenv_owner: "{{ username }}"

License
-------

MIT

Author Information
------------------

Glen Jarvis <glen@glenjarvis.com>. This role is included as an exercise in
"Ansible Hands On," a hands-on training program that teaches Ansible through
examples. Therefore, some roles will not be optimized as students may not have
yet encountered the skill that could better optimize this role.
