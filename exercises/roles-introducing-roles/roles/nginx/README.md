nginx
=====

Install Nginx webserver and configure to listen to and serve upstream service
(http://{{ nginx_server_host }}:{{ 8000}}/)

Requirements
------------

This role was created as an exercise in a training program. Although we could
dynamically handle different packaging tools, at this stage in the learner's
path, we keep it simple to only using the "yum" package manager.

Therefore, this should be an Amazon Linux, RedHat, Centos, or other
distribution that can install the *nginx* package via YUM. In the learner's
future path, we will see how to make this more dynamic and fetch the packages
and installation method via operating system.


Role Variables
--------------

The following are default variables:

nx_user: nginx
nginx_non_privileged_user: nginx
nginx_server_name: www.example.com
nginx_server_host: 127.0.0.1
nginx_server_port: 8000
nginx_log_dir: /var/log/nginx
nginx_static_dir: /local/static
nginx_media_dir: /local/media

All variables can safely be overridden. The most common variables to overwrite
are:

nginx_non_privileged_user: This is the user that owns static files (e.g., web).
			   This is generally used as a loose coupling for
			   upstream systems (e.g., Django)

nginx_server_name: This is the virtual DNS name for the system to be served.
                   You will probably be serving on another location instead of
                   http://www.example.com/.

nginx_server_port: The upstream port to listen. This is generally loosely coupled
                   with an upstream system (e.g., Django).


Dependencies
------------

None

Example Playbook
----------------

    - hosts: webservers
      vars:
        - username: web
      roles:
        - role: nginx
          nginx_user: nginx
          nginx_non_privileged_user: "{{ username }}"


License
-------

MIT

Author Information
------------------

Glen Jarvis <glen@glenjarvis.com>. This role is included as an exercise in
"Ansible Hands On," a hands-on training program that teaches Ansible through
examples. Therefore, some roles will not be optimized as students may not have
yet encountered the skill that could better optimize this role.
