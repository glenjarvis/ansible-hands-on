=========================
Ansible Hands-On Training
=========================

A tutorial with video and code taking the user from AWS machine creation to their first deployment using Ansible

************************
Project and Build Status
************************

.. image:: https://travis-ci.org/glenjarvis/ansible_tutorial.svg?branch=master
     :target: https://travis-ci.org/glenjarvis/ansible_tutorial
     :alt: Travis tests

.. image:: https://pyup.io/repos/github/glenjarvis/ansible_tutorial/shield.svg
     :target: https://pyup.io/repos/github/glenjarvis/ansible_tutorial/
     :alt: Updates

.. image:: https://pyup.io/repos/github/glenjarvis/ansible_tutorial/python-3-shield.svg
     :target: https://pyup.io/repos/github/glenjarvis/ansible_tutorial/
     :alt: Python 3

.. image:: https://readthedocs.org/projects/ansible_tutorial/badge/?version=latest
     :target: http://ansible_tutorial.readthedocs.io/en/latest/?badge=latest
     :alt: Documentation Status

.. There is currently a problem at Appveyor
.. .. image:: https://ci.appveyor.com/api/projects/status/github/glenjarvis /ansible_tutorial?branch=master&svg=true
      :target: https://ci.appveyor.com/project/glenjarvis/ansible_tutorial/branch/master
      :alt: Windows build status on Appveyor

**This Repository is now out of date**. This was written against an older
version of Ansible. The build looks like it passes, but that is because this is
out of date. I am writing this note on 18-May, 2018 and hope to get to upgrading
this repository to work with current versions of Ansible. This issue tracks:

https://github.com/glenjarvis/ansible_tutorial/issues/78


* GitHub repo: https://github.com/glenjarvis/ansible_tutorial/
* Documentation: `Read The Docs <https://ansible_tutorial.readthedocs.io/>`_
* Free software: `LICENSE <https://github.com/glenjarvis/ansible_tutorial/blob/master/LICENSE>`_


*******
Welcome
*******

A tutorial with video and code taking the user from AWS machine creation to their first deployment using Ansible


Successfully automating your machines in the cloud using Ansible
================================================================


Videos of Talk
--------------

Prerequisite Talks
^^^^^^^^^^^^^^^^^^

* `Building an AWS Instance <https://www.youtube.com/watch?v=tmNgXQXkpWs>`_


Slow Walkthrough
^^^^^^^^^^^^^^^^

Same material / Digestible pace / Longer Video:

* 9-Aug, 2014 `Hands-On Training
  <https://www.youtube.com/watch?v=w8fOEEMqpOw>`__


Fast Overview
^^^^^^^^^^^^^

Same material / Quickly covered / Shorter Video:

* 26-June, 2014 `Bay Area Python Interest Group (BayPIGgies)/Silicon Valley Python MeetUp Video <https://plus.google.com/hangouts/onair/watch?hid=hoaevent%2Fcf7vrv1f9q5e8bojpslfjjen8gk&ytl=ptzruazbRXY&hl=en>`_


Practice Sessions
^^^^^^^^^^^^^^^^^

**This Repository is now out of date**. This was written against an older
version of Ansible and hasn't yet been updated. I am writing this note on
18-May, 2018 and hope to get to upgrading this repository to work with current
versions of Ansible. This issue tracks:

https://github.com/glenjarvis/ansible_tutorial/issues/78


Hands-On Training
^^^^^^^^^^^^^^^^^
  - No sessions currently scheduled


Talk description
----------------

As we have seen with the previous talk, "Red Pill, Blue Pill Virtual Machines
and Virtual Environments" (`GitHub
<https://github.com/glenjarvis/red-pill-blue-pill>`_ / `YouTube
<https://www.youtube.com/watch?v=xZb3cr1JrMg>`_), we can create virtual machines
in the cloud.

But, how do you "stamp" those machines differently? If you need to build a web
server, mail server, DNS server, and load balancer, each machine may have the
same base image but needs to be configured differently.

If you manually configure those machines, what happens when you suddenly have a
surge in traffic and need four more web servers? Or, what if one finds a
vulnerability in a library like `Heartbleed
<http://en.wikipedia.org/wiki/Heartbleed>`_ in OpenSSL? A very safe option would
be to rebuild these machines from scratch. If they were built manually,
rebuilding these machines within minutes from scratch would be daunting, tedious
and error prone.

There are several tools that have been built to fix this problem. Two of the
most popular tools, `Chef <http://www.getchef.com>`__ and `Puppet
<http://puppetlabs.com/puppet/what-is-puppet>`_, are written in the `Ruby
<https://www.ruby-lang.org/>`_ programming language. And, especially for the
most popular, `Chef <http://www.getchef.com>`_, one needs somewhat of a
familiarity with that language to use the tool.

There are two more tools that are written in `Python <https://www.python.org/>`_
and are growing in popularity: `Salt <http://www.saltstack.com/>`_ and `Ansible
<http://www.ansible.com/>`__.  `Ansible <http://www.ansible.com/>`__ requires
the least amount of set-up (if any) and has the simplest infrastructure (it
simply uses commands over ssh like `Fabric <http://www.fabfile.org/>`_ does).
`Ansible <http://www.ansible.com/>`__ is the easiest tool to get started with if
you are new in the machine build automation frameworks.

We will start with a newly built machine and obtain it's public IP address. We
will configure the `ansible_hosts` file with the IP address, and add/build plays
(like recipes) to gradually configure that machine so that it is a
`Django <https://www.djangoproject.com/>`_ web server running in the cloud. When
we are finished, we should have a running machine and a recipe to easily build a
seconded machine with a few keystrokes.

P.S. If you haven't previously built an `Amazon Web Instance
<http://aws.amazon.com/>`_, I highly recommend `watching this video
<https://www.youtube.com/watch?v=tmNgXQXkpWs>`_ in advance of the talk.


Getting Started (Installing and following-along)
------------------------------------------------

**This Repository is now out of date**. This was written against an older
version of Ansible and hasn't yet been updated. I am writing this note on
18-May, 2018 and hope to get to upgrading this repository to work with current
versions of Ansible. This issue tracks:

https://github.com/glenjarvis/ansible_tutorial/issues/78


1. Clone this repo.

   ..code:: bash

       $ git clone https://github.com/glenjarvis/ansible_tutorial.git
       Cloning into 'ansible_tutorial'...
       remote: Reusing existing pack: 112, done.
       remote: Total 112 (delta 0), reused 0 (delta 0)
       Receiving objects: 100% (112/112), 37.58 KiB | 0 bytes/s, done.
       Resolving deltas: 100% (48/48), done.
       Checking connectivity... done.


2. Make a virtualenv named **venv** for your Python environment of choice.

    * For Python2::

        $ virtualenv venv

    * For Python3::

        $ python3 -m venv venv

3. Activate the Virtual Enviroment. Every time you come back to work on this
   project, you will need to activate your virtual environment::

       $ cd full_path_to_this_repo
       $ source venv/bin/activate

   When the Virtual Environment is activated, you should see ``venv`` in the
   prompt. It may look something  to this::

       (venv) $

   I often like to be able to jump to this folder quickly from
   anywhere and have it automatically setup my virtual environment.
   So, I put something like this in my ``$HOME/.bashrc`` (or equivalent)
   file:

   .. code-block:: bash

       function cd_ansible_tutorial {
           deactivate 2> /dev/null
           cd /FULL_PATH_TO_THIS_DIRECTORY
           source venv/bin/activate
       }

4. Upgrade Pip. The Pip that comes with a new Virtual Environment is often too
   old. Upgrade it to be sure it is current:

   .. code-block:: bash

       (venv)$ pip install --upgrade pip
       Collecting pip
         Using cached https://files.pythonhosted.org/packages/0f/74/ecd13431bcc456ed390b44c8a6e917c1820365cbebcb6a8974d1cd045ab4/pip-10.0.1-py2.py3-none-any.whl
       Installing collected packages: pip
         Found existing installation: pip 9.0.3
           Uninstalling pip-9.0.3:
             Successfully uninstalled pip-9.0.3
       Successfully installed pip-10.0.1


5. Configure the repo for your account and settings

   .. code-block:: bash

       (venv)$ ( cd src; python configure.py )

       This script creates configuration files for using Ansible to
       configure a newly-created virtual machine.
       It has been tested by the author on an AWS free tier VM.
       This has the best chance of working on an AWS free tier VM, or
       failing that, on a VM with a recent version of CentOS.

       No configuration file found. Let me ask questions so that we can configure.

       What is the path to your .pem key file for  the virtual machine?
       --> ~/example_key.pem

       What user to use to ssh to the remote system [ec2-user]?
       -->
       Configuring `ansible_hosts` file ./ansible_hosts...

       What is the IP address of the virtual machine?
       --> demos.glenjarvis.com

       Configuration is complete.

6. Follow the examples (starting with the ``example_01`` subdirectory).


Examples
--------

Here is a list of the examples just in case there's any confusion in which
order the examples should be executed:

1. ``( cd src; python configure.py )`` (see instructions above)
2. ``( cd src/example_01; python access_machine.py )``
3. ``( cd src/example_02; python auto_update_machine.py )``
4. ``( cd src/example_03; less README.txt )`` (Read the ``README.txt`` file; it's not really meant to be executed)
5. ``( cd src/example_04; ansible webservers -m ping; ansible webservers -vvv -m ping )``
6. ``( cd src/example_05; ansible webservers -vvv -a 'sudo yum update -y' )``
7. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_01.yml )``
8. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_02.yml )``
9. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_03.yml )``
10. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_04.yml )``
11. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_05.yml )``
12. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_06.yml )``
13. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_07.yml )``
14. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_08.yml )``
15. ``( cd src/playbook_examples; ansible-playbook demo_playbook_iter_09.yml )``
16. ``( cd src/playbook_examples; less pedantically_commented_playbook )`` (Read but don't execute: ``pedantically_commented_playbook.yml``)
17. ``( cd src/role_examples; ansible-playbook demo_play_role_01.yml )``
18. ``( cd src/role_examples; ansible-playbook demo_play_role_02.yml )``
19. ``( cd src/role_examples; ansible-playbook demo_play_role_03.yml )``
20. Exploration: Log into machine; ``sudo su - webuser; cd /home/webuser/sample_project; python manage.py runserver``


Bio
---

Glen has been a Python programmer since 2007 and has worked for
companies such as IBM, UC Berkeley, Sprint, Informix, and many start-ups.
He has also worked both in the US and in the UK and has had Bioinformatics
research published in `Nucleic Acids Research (Oxford
Journals) <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2896197/>`_ He is a
certified DBA and has also been certified in Linux/Unix Administration.

He is a DevOps engineer and uses `Ansible <http://www.ansible.com/home>`__
heavily. After five years, he just finished working for a startup. He is
creating a Coursera course in collaboration with a UC campus on Source Code
Mangement Systems for the DevOps developer.

Additionally, he runs a small start up, `Glen Jarvis Training & Consulting, LLC
<http://glenjarvis.com/>`_, that does online technical training and assists
employees obtaining telepresence in their current work place.

Glen is the organizer for the `Silicon Valley Python MeetUp
Group <http://www.meetup.com/silicon-valley-python/>`_ and a co-organizer of the
`Bay Area Python Interest Group <http://baypiggies.net/>`_.

More information:

* `GlenJarvis.com <https://glenjarvis.com>`_

* `GitHub <https://github.com/glenjarvis/>`__

* `Google+ <https://plus.google.com/u/0/+GlenJarvis/posts>`_

* `LinkedIn <http://www.linkedin.com/in/glenjarvis>`_




********************************
Make this better by Contributing
********************************

This is an Open Source project and contributions are always welcome, and they
are greatly appreciated! Every little bit helps, and credit will always be
given.

You can contribute in many ways:

* `Report bugs <https://github.com/glenjarvis/ansible_tutorial/issues>`__
* `Write Documentation <https://ansible_tutorial.readthedocs.io/>`__
* `Fix bugs <https://github.com/glenjarvis/ansible_tutorial/issues>`__

To maximize the chance that your hard work gets merged, we have these guidelines
to guide you along the way to a successfully merged Pull Request:

* :ref:`contribution_link`
* https://github.com/glenjarvis/ansible_tutorial/blob/master/CONTRIBUTING.rst
