#!/usr/bin/env python
# ** magic is intentional; pylint: disable=W0142


"""Example 04: Configure the ansible demo for your first ansible deploy

This simply takes the machine name and the AWS key and configures the
ansible_hosts.

The example ping command assumes a python environment (or active
virtual environment) with these packages installed:
  - paramiko
  - PyYAML
  - jinja2
  - httplib2
  - ansible

If you have a custom virtualenv (not default for basic shell), then you
may also have to manually configure the `ansible_python_interpreter`
parameter (like we automatically configure the
`ansible_ssh_private_key_file` parameter).
"""

import os
import sys
import subprocess

ANSIBLE_HOSTS_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'ansible_hosts')


def configure():
    """An example to show how one executes remote commands via ssh"""

    args = {}

    print "Configuring `ansible_hosts` file...\n\n"
    print "What is the path to your Amazon pem key?"
    args['pem_file_path'] = raw_input('--> ')

    if not os.path.exists(args['pem_file_path']):
        print "Nope. This file cannot be found: {pem_file_path}".format(**args)
        sys.exit(1)

    print "\n\nWhat is the IP address of the Amazon Linux free tier machine?"
    args['machine_address'] = raw_input('--> ')
    args['pkf'] = "ansible_ssh_private_key_file"
    entry = "{machine_address} {pkf}={pem_file_path}\n".format(**args)

    with open(ANSIBLE_HOSTS_FILE, 'w') as ansible_hosts_file:
        ansible_hosts_file.write("[webservers]\n")
        ansible_hosts_file.write(entry)

    print "\n"


def check_and_configure():
    """Check if `ansible_hosts` file exists; Configure if it doesn't"""

    if not os.path.exists(ANSIBLE_HOSTS_FILE):
        configure()


def example_04():
    """Configure `ansible_hosts` and run ansible ping command"""

    os.environ['ANSIBLE_HOSTS'] = ANSIBLE_HOSTS_FILE
    cmd = "ansible webservers -m ping -u ec2-user"
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    check_and_configure()
    example_04()
