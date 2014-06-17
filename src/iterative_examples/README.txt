The training wheels are off!
============================

In example_04 and example_05, we asked the information for the ansible_hosts
file, created it for you, and ran the commands.

This example uses ansible without any helping scripts.

Note, that you will have to set an environment variable to tell ansible where
the `ansible_hosts` file is:

```
prompt> source ./env.sh 
prompt> ansible-playbook example_06_playbook.yml

PLAY [webservers] ************************************************************* 

GATHERING FACTS *************************************************************** 
ok: [demos.glenjarvis.com]

TASK: [Make sure all OS patches are applied] ********************************** 
changed: [demos.glenjarvis.com]

PLAY RECAP ******************************************************************** 
demos.glenjarvis.com           : ok=2    changed=1    unreachable=0    failed=0   
```



Tired of fiddling with `ansible_hosts`?
=======================================
This is meant to be a centralized host file. And, we only have one host in it
for this demo. There are default locations for this file. For example, you
could configure this file in /etc/ansible/hosts (you will probably need admin
privileges).

I didn't feel comfortable writing files outside of this repository (that way
you can cleanly throw everything away if you choose). 

But, if you get tired of fiddling, you can always set it in the system.
