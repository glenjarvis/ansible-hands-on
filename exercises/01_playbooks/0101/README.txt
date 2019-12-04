Exercise 0101 - Adding tasks
============================

We now start using Ansible playbooks. Notice the contents of the `playbook_0101.yml` file:

---
- hosts: demoserver
  tasks:
    - name: Make sure all OS patches are applied
      shell: yum update -y
      become: yes
    - name: Install our needed packages for AWS Linux
      shell: yum install -y git
      become: yes


Play the playbook with the command:

ansible-playbook playbook_0101.yml

You should see output similar to what is in the `output_0101.txt` file in this directory.
