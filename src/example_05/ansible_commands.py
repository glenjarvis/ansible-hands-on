#!/usr/bin/env python
# ** magic is intentional; pylint: disable=W0142


"""Example 05: Do 'yum update -y

Configure `ansible_hosts` if it doesn't exist. See notes in
example_05.py for dependencies.
"""

import os
import sys
import subprocess

ANSIBLE_HOSTS_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../iterative_examples/ansible_hosts')  # This is not a mistake (we will use in 6)


def check_ansible_hosts():
    """Check if `ansible_hosts` file exists"""

    if not os.path.exists(ANSIBLE_HOSTS_FILE):
        print "We are trying to use the `ansible_hosts` file from"
        print "iterative_examples directory. But, we can't find it. Doh!"
        sys.exit(1)


def example_05():
    """Configure `ansible_hosts` and run ansible ping command"""

    print "Executing ansible command"
    os.environ['ANSIBLE_HOSTS'] = ANSIBLE_HOSTS_FILE
    cmd = "ansible webservers -u ec2-user -a 'sudo yum update -y'"
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    check_ansible_hosts()
    example_05()
