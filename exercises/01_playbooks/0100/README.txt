The training wheels are off!
============================

We now start using Ansible playbooks. Notice the contents of the `playbook_0100.yml` file:

---
- hosts: demoserver
  tasks:
    - name: Make sure all OS patches are applied
      shell: yum update -y
      become: yes

