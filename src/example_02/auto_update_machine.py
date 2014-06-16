#!/usr/bin/env python
# ** magic is intentional; pylint: disable=W0142


"""Example 02: Automatically update system packages

This is only a placeholder to help new participants understand how
remote ssh commands are executed. Like the previous exercise, they will need to
have two things:

  1) The IP address of the machine created (that hasn't had sudo yum update -y)
  2) The key file used to access the machine (with correct permissions).
"""

import os
import sys
import subprocess


def example_02():
    """An example to show how one executes remote commands via ssh"""

    args = {}

    print "What is the path to your Amazon pem key?"
    args['pem_file_path'] = raw_input('--> ')

    if not os.path.exists(args['pem_file_path']):
        print "Nope. This file cannot be found: {pem_file_path}".format(**args)
        sys.exit(1)

    print "\n\nWhat is the IP address of the Amazon Linux free tier machine?"
    args['machine_address'] = raw_input('--> ')

    old_cmd = "ssh -i {pem_file_path} ec2-user@{machine_address}".format(**args)
    new_cmd = "{0} -t 'sudo yum update -y'".format(old_cmd)

    print "\nCommand to execute: {}\n\n".format(new_cmd)

    subprocess.call(new_cmd, shell=True)

    print "\n"

if __name__ == '__main__':
    example_02()
