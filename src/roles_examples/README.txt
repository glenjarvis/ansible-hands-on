Welcome to the "Tour de France"
===============================
(remember when you had training wheels)

Old playbooks now became roles (like a playbook split into smaller pieces for
easier management). And, new playbooks use these old playbooks. How Meta!


Roles
=====
Review these roles:

* common
* app_server_django
* python_stack
* web_server_nginx


Examples
========
1. ansible-playbook demo_play_role_01.yml
2. ansible-playbook demo_play_role_02.yml 
   - Try to access a web page on your machine
3. ansible-playbook demo_play_role_03.yml
   - Log into machine!; sudo su - webuser; cd /home/webuser/sample_project; python manage.py runserver
   - Explore!


BONUS
=====
We have a super example that we haven't even been talking about yet. We're
going to spend time talking about. I'm going to talk about
library/ssh_secondary_access so that you can see how to create your own modules.
