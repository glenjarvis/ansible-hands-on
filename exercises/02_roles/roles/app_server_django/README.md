Role Name
=========

This role installs a walking skeleton of a Django app.  Note that this is a
teaching exercise in Ansible roles.

If this were a real role, we sould interface with an outside source repository
for the Django code to deploy. This repository would have:

  - a `requirements.txt` file for modules to isntall via pip, 
  - The Django source (usually fetched via Git)
  - etc.

Requirements
------------

This role expects a Python virtual environment as specified in the
`django_virtualenv_dir` variable (see below). This is loosly coupled with a
role such as `python3_6` (which ensures the creation of a Python virtual
environment).

Role Variables
--------------

The following are default variables:

django_virtualenv_dir: /local/pythonvenv/venv
django_user: django
django_group: django
django_app_path: /local/app_server


Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }


    - hosts: webservers
      vars:
        - username: web
        - virtualenv_root: /local/pythonvenv
      roles:
        - role: non_priviledged_user
          non_priviledged_user_name: "{{ username }}"
          non_priviledged_user_uid: 1100

        - role: python3_6
          python_virtualenv_root: "{{ virtualenv_root }}"
          python_virtualenv_owner: "{{ username }}"

        - role: app_server_django
          django_app_path: /local/app_server
          django_user: "{{ username }}"
          django_group: "{{ username }}"
          django_virtualenv_dir: "{{ virtualenv_root }}/venv"

License
-------

MIT

Author Information
------------------

Glen Jarvis <glen@glenjarvis.com>. This role is included as an exercise in
"Ansible Hands On," a hands-on training program that teaches Ansible through
examples. Therefore, some roles will not be optimized as students may not have
yet encountered the skill that could better optimize this role.
