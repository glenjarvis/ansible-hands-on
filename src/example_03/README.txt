We now have established that we can issue ssh commands remotely.

We can also copy files securely between systems. This is how Ansible works. It
will create a Python module, copy it to the remote machine, and then execute
that module.

Here is a module that I caught before it finished executing and was removed:

/home/ec2-user/.ansible/tmp/ansible-tmp-1399757000.18-123070607653156/command

Looks what happens when I try to run it outside of this environment on a
machine that doesn't understand yum (I renamed it ansible_module.py for clarity):

lappy> python ansible_module.py
{"msg": "[Errno 2] No such file or directory", "failed": true, "cmd": "yum update", "rc": 2}

Notice some of these bits:

 # == BEGIN DYNAMICALLY INSERTED CODE ==

 MODULE_ARGS = 'yum update'
 MODULE_COMPLEX_ARGS = '{}'

 BOOLEANS_TRUE = ['yes', 'on', '1', 'true', 1]
 BOOLEANS_FALSE = ['no', 'off', '0', 'false', 0]
 BOOLEANS = BOOLEANS_TRUE + BOOLEANS_FALSE

 # ansible modules can be written in any language.  To simplify
 # development of Python modules, the functions available here
 # can be inserted in any module source automatically by including
 # #<<INCLUDE_ANSIBLE_MODULE_COMMON>> on a blank line by itself inside
 # of an ansible module. The source of this common code lives
 # in lib/ansible/module_common.py

See the ./ansible_module.py file in this same directory for a full capture of the output.
