# Successfully automating your machines in the cloud using Ansible

As we have seen with the previous talk, "Red Pill, Blue Pill Virtual Machines
and Virtual Environments"
( [GitHub](https://github.com/glenjarvis/red-pill-blue-pill) /
  [YouTube](https://www.youtube.com/watch?v=xZb3cr1JrMg) ), we can create
virtual machines in the cloud.

But, how do you "stamp" those machines differently? If you need to build a web
server, mail server, DNS server, and load balancer, each machine may have the
same base image but needs to be configured differently.

If you manually configure those machines, what happens when you suddenly have a
surge in traffic and need four more web servers? Or, what if one finds a
vulnerability in a library like
[Heartbleed](http://en.wikipedia.org/wiki/Heartbleed) in OpenSSL as we recently
encountered. A very safe option would be to rebuild these machines from
scratch. If they were built manually, rebuilding these machines within minutes
from scratch would be daunting, tedious and error prone.

There are several tools that have been built to fix this problem. Two of the
most popular tools ([Chef](http://www.getchef.com/) and
[Puppet](http://puppetlabs.com/puppet/what-is-puppet) ) are written in the
[Ruby](https://www.ruby-lang.org/) programming language. And, especially for
the most popular, [Chef](http://www.getchef.com/), one needs somewhat of a
familiarity with that language to use the tool.

There are two more tools that are written in [Python](https://www.python.org/)
and are growing in popularity: [Salt](http://www.saltstack.com/) and
[Ansible](http://www.ansible.com/).  [Ansible](http://www.ansible.com/)
requires the least amount of set-up (if any) and has the simplest
infrastructure (it simply uses commands over ssh like
[Fabric](http://www.fabfile.org/) does). [Ansible](http://www.ansible.com/) is
the easiest tool to get started with if you are new in the machine build
automation frameworks.

We will start with a newly built machine and obtain it's public IP address. We
will configure the `ansible_hosts` file with the IP address, and add/build plays
(like recipes) to gradually configure that machine so that it is a
[Django](https://www.djangoproject.com/) web server running in the cloud. When
we are finished, we should have a running machine and a recipe to easily build
a seconded machine with a few keystrokes.

P.S. If you haven't previously built an [Amazon Web
Instance](http://aws.amazon.com/), I highly recommend [watching this
video](https://www.youtube.com/watch?v=xZb3cr1JrMg) in advance of the talk.


## Getting Started (Installing and following-along)

1. Clone this repo.

    ```bash
    prompt> git clone https://github.com/glenjarvis/ansible_tutorial.git
    Cloning into 'ansible_tutorial'...
    remote: Reusing existing pack: 112, done.
    remote: Total 112 (delta 0), reused 0 (delta 0)
    Receiving objects: 100% (112/112), 37.58 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (48/48), done.
    Checking connectivity... done.
    ```

2. Change to the src directory.

    ```bash
    prompt> cd ansible_tutorial
    ```

3. Configure the repo for your account and settings

    ```bash
    prompt> ( cd src; python configure.py )

        No configuration file found. Let me ask questions so that we can configure.

    What is the path to your Amazon pem key?
    --> example_key.pem

    Configuring `ansible_hosts` file ./ansible_hosts...

    What is the IP address of the Amazon Linux free tier machine?
    --> demo.example.com

    Configuration is complete.
    ```

4. Follow the examples (starting with the `example_01` subdirectory).

## Examples

Here is a list of the examples just in case there's any confusion in which
order the examples should be executed:

1. `( cd src; python configure.py )` (see instructions above)
2. `( cd src/example_01; python access_machine.py )`
3. `( cd src/example_02; python auto_update_machine.py )`
4. `( cd src/example_03; less README.txt )` (Read the `README.txt` file; it's not really meant to be executed)
5. `( cd src/example_04; ansible webservers -m ping; ansible webservers -vvv -m ping )`
6. `( cd src/example_05; ansible webservers -a 'sudo yum update -y' )`
7. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_01.yml )`
8. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_02.yml )`
9. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_03.yml )`
10. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_04.yml )`
11. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_05.yml )`
12. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_06.yml )`
13. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_07.yml )`
14. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_08.yml )`
15. `( cd src/playbook_examples; ansible-playbook demo_playbook_iter_09.yml )`
16. `( cd src/playbook_examples; less pedantically_commented_playbook )` (Read but don't execute: `pedantically_commented_playbook.yml`)
17. `( cd src/role_examples; ansible-playbook demo_play_role_01.yml )`
18. `( cd src/role_examples; ansible-playbook demo_play_role_02.yml )`
19. `( cd src/role_examples; ansible-playbook demo_play_role_03.yml )`
20. Exploration: Log into machine; `sudo su - webuser; cd /home/webuser/sample_project; python manage.py runserver`

## Bio
Glen has been a full-time Python programmer since 2007 and has worked for
companies such as IBM, UC Berkeley, Sprint, Informix, and many small start-ups.
He has also worked both in the US and in the UK and has had Bioinformatics
research published in [Nucleic Acids Research (Oxford
Journals)](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2896197/). He is a
certified DBA and has also been certified in Linux/Unix Administration.

He currently works for a start-up, [RepairPal](http://repairpal.com/) (for
accurate car repair prices) using [Ruby on Rails](http://rubyonrails.org/) and
[Ansible](http://www.ansible.com/home).  Additionally, he runs a small start
up, [Glen Jarvis, LLC](http://glenjarvis.com/), that does online technical
training and assists employees obtaining telepresence in their current work
place.

Glen is the organizer for the [Silicon Valley Python MeetUp
Group](http://www.meetup.com/silicon-valley-python/) and an active member in
the [Bay Area Python Interest Group](http://baypiggies.net/) organization.

[GitHub](https://github.com/glenjarvis/)

[Google+](https://plus.google.com/u/0/+GlenJarvis/posts)

[LinkedIn](http://www.linkedin.com/in/glenjarvis)



### Documentation for configure.py (if needed)

Although this probably won't be needed, here is the `configure.py`
documentation that is used to help you configure your `ansible.cfg` and
`ansible_hosts` files.


```python
Help on module configure:

NAME
    configure - Configure the demo repository to make it easier to learn/follow

FILE
    ...ansible-tutorial/src/configure.py

DESCRIPTION
    This takes the machine name and the AWS pem key path and configures the
    ansible.cfg and ansible_hosts files. We also avoid the most common
    gotcha (permissions on the downloaded key file) by setting the
    permissions to be Read/Write for only the owner.

FUNCTIONS
    check_and_configure()
        Check/configure `ansible.cfg` and `ansible_hosts`
    
    configure_config()
        Assuming no ansible.cfg exists, ask questions and create a new one
    
    configure_hosts(hostfile)
        Assuming no hostfile file exists, ask questions and create a new one
    
    fix_pem_permissons(pem_file_path)
        Forcefully fix the PEM file permissions
        
        The larest problem that new users have when connecting ot their
        first AWS instance is that the permissions on the *.pem key that
        they downloaded is too permissive. It really isn't a *private* key
        if anyone else on the system (group or other) can read the file.
        
        We change the permissions to the file given so that only the owner
        can read or write. There really isn't a reason to allow write
        permissions for the key, however, these are the default permissions
        for an ssh key.
    
    get_configured_hosts()
        Read the ansible.cfg file and parse hostfile pathname
    
    write_ansible_cfg_file(pem_file_path)
        Given a validated pem_file_path, write the ansible configuration file

DATA
    ANSIBLE_CONFIG_FILENAME = './ansible.cfg'
    ANSIBLE_CONFIG_FILEPATH = '...ansible-tutorial/src/ansible.cfg'
    ANSIBLE_HOSTS_FILENAME = './ansible_hosts'
    ANSIBLE_HOSTS_FILEPATH = '...ansible-tutorial/src/ansible_hosts'
    BASE_FILE = '...ansible-tutorial/src'
```
