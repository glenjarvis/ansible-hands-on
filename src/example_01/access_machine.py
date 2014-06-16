#!/usr/bin/env python
# ** magic is intentional; pylint: disable=W0142


"""Example 01: Basic access to AWS machine

This is only a placeholder to help new participants understand the
ommand on how to access their AWS machine. They will need to have two
things:

  1) The IP address of the machine created
  2) The key file used to access the machine (with correct permissions).
"""

import os
import sys
import subprocess


def example_01():
    """An example to show how one connects to their EC2 instance"""

    args = {}

    print "What is the path to your Amazon pem key?"
    args['pem_file_path'] = raw_input('--> ')

    if not os.path.exists(args['pem_file_path']):
        print "Nope. This file cannot be found: {pem_file_path}".format(**args)
        sys.exit(1)

    print "\n\nWhat is the IP address of the Amazon Linux free tier machine?"
    args['machine_address'] = raw_input('--> ')

    cmd = "ssh -i {pem_file_path} ec2-user@{machine_address}".format(**args)

    print "\nCommand to execute: {}\n\n".format(cmd)

    subprocess.call(cmd, shell=True)

    print "\n"

if __name__ == '__main__':
    example_01()
