The training wheels are off!
============================

We now start using Ansible playbooks. Notice the contents of the `playbook_0100.yml` file:

---
- hosts: demoserver
  tasks:
    - name: Make sure all OS patches are applied
      shell: yum update -y
      become: yes


Play the playbook with the command:

ansible-playbook playbook_0100.yml


You should see output similar to what is in the `output_0100.txt` file in this directory.
