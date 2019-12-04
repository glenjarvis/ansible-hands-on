non_priviledged_user
====================

When certain web processes are public facing, they should be run by a
non-privledged user (i.e., no sudo or root access). This role ensures the
creation of that user.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

The userid (uid) of the user should not already exist. Default uid is specified
in Role Variables section below.  Currently, this module does not allow the
userid assignment to be done by the operating system.

Role Variables
--------------

The following two variables are used to modify the name and uid of the
non-priviledged user. The following are the default values if not provided.

non_priviledged_user_name: web
non_priviledged_user_uid: 1100


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

License
-------

MIT

Author Information
------------------

Glen Jarvis <glen@glenjarvis.com>. This role is included as an exercise in
"Ansible Hands On," a hands-on training program that teaches Ansible through
examples. Therefore, some roles will not be optimized as students may not have
yet encountered the skill that could better optimize this role.

