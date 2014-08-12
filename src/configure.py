#!/usr/bin/env python


"""Configure the demo repository to make it easier to learn/follow

This takes the machine name and the AWS pem key path and configures the
ansible.cfg and ansible_hosts files. We also avoid the most common
gotcha (permissions on the downloaded key file) by setting the
permissions to be Read/Write for only the owner.
"""

import ConfigParser
import os
import stat
import sys

BASE_FILE = os.path.dirname(os.path.abspath(__file__))
ANSIBLE_HOSTS_FILENAME = './ansible_hosts'
ANSIBLE_HOSTS_FILEPATH = os.path.join(BASE_FILE, ANSIBLE_HOSTS_FILENAME)
ANSIBLE_CONFIG_FILENAME = './ansible.cfg'
ANSIBLE_CONFIG_FILEPATH = os.path.join(BASE_FILE, ANSIBLE_CONFIG_FILENAME)


def fix_pem_permissons(pem_file_path):

    """Forcefully fix the PEM file permissions

    The largest problem that new users have when connecting ot their
    first AWS instance is that the permissions on the *.pem key that
    they downloaded is too permissive. It really isn't a *private* key
    if anyone else on the system (group or other) can read the file.

    We change the permissions to the file given so that only the owner
    can read or write. There really isn't a reason to allow write
    permissions for the key, however, these are the default permissions
    for an ssh key.
    """
    os.chmod(pem_file_path, stat.S_IRUSR | stat.S_IWUSR)


def write_ansible_cfg_file(pem_file_path, user):

    """Given a validated pem_file_path, write the ansible configuration file"""

    fix_pem_permissons(pem_file_path)
    config = ConfigParser.RawConfigParser()
    config.add_section('defaults')
    config.set('defaults', 'hostfile', ANSIBLE_HOSTS_FILENAME)
    config.set('defaults', 'private_key_file', pem_file_path)
    config.set('defaults', 'remote_user', user)

    with open(ANSIBLE_CONFIG_FILENAME, 'wb') as config_file:
        config.write(config_file)


def configure_config():

    """Assuming no ansible.cfg exists, ask questions and create a new one"""

    print """
    No configuration file found. Let me ask questions so that we can configure.
    """

    print "What is the path to your .pem key file for the virtual machine?"
    print "Be sure to include the filename in the path."
    pem_file_path = raw_input('--> ')
    pem_file_path = pem_file_path.strip()
    pem_file_path = os.path.expanduser(pem_file_path)  # expand ~user

    if os.path.isdir(pem_file_path):
        print "We mean the path to (including the file name)."
        print "You have entered a directory, but no file name: {0}".format(
            pem_file_path)
        sys.exit(1)

    if not os.path.exists(pem_file_path):
        print "Nope. This file cannot be found: {0}".format(pem_file_path)
        sys.exit(1)

    print """\nYou are now being given the opportunity of over-riding
    the 'ec2-user' default user name.  Unless you know what you are doing,
    and specifically want to change the user name, please just hit the 
    <Enter> key without making any other entry."""
    user = raw_input('--> ') or 'ec2-user'
    user = user.strip()

    write_ansible_cfg_file(pem_file_path, user)


def get_configured_hosts():

    """Read the ansible.cfg file and parse hostfile pathname"""

    config = ConfigParser.SafeConfigParser()
    config.read(ANSIBLE_CONFIG_FILENAME)

    hostfile = config.get('defaults', 'hostfile')
    if hostfile is None:
        print "We can't read the hostfile settings from {0}".format(
            ANSIBLE_CONFIG_FILENAME)
        sys.exit(2)

    return hostfile


def configure_hosts(hostfile):

    """Assuming no hostfile file exists, ask questions and create a new one"""

    print "Configuring `ansible_hosts` file {0}...\n".format(hostfile)

    print "What is the IP address of the virtual machine?"
    machine_address = raw_input('--> ')
    machine_address = machine_address.strip()

    with open(hostfile, 'w') as ansible_hosts_file:
        ansible_hosts_file.write("[webservers]\n")
        ansible_hosts_file.write("{0}\n".format(machine_address))


def check_and_configure():
    """Check/configure `ansible.cfg` and `ansible_hosts`"""

    print "\nThis script creates configuration files for using Ansible to "
    print "configure a newly-created virtual machine."
    print "It has been tested by the author on an AWS free tier VM."
    print "This has the best chance of working on an AWS free tier VM, or "
    print "failing that, on a VM with a recent version of CentOS."

    if not os.path.exists(ANSIBLE_CONFIG_FILEPATH):
        configure_config()

    # Re-read the hosts from the config file in case it is changed by
    # the user
    hostfile = get_configured_hosts()

    if not os.path.exists(hostfile):
        configure_hosts(hostfile)

    print "\nConfiguration is complete."


if __name__ == '__main__':
    check_and_configure()
