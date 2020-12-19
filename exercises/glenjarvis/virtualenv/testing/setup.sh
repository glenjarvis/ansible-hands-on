#!/usr/bin/bash

curl https://pyenv.run | bash
export PATH="/home/user/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install 3.8.6
PYENV_VERSION=3.8.6 pyenv virtualenv ansible_testing
source ~/.pyenv/versions/ansible_testing/bin/activate
/home/user/.pyenv/versions/3.8.6/envs/ansible_testing/bin/pip install --upgrade pip
/home/user/.pyenv/versions/3.8.6/envs/ansible_testing/bin/pip install ansible
/home/user/.pyenv/versions/3.8.6/envs/ansible_testing/bin/ansible-galaxy install amazon.aws
ls ~/.ansible/collections/ansible_collections/
ansible-playbook test.yml
