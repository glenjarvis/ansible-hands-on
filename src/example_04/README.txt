You should be able to ping your "webservers" (the host that you previously
configured). Just run this command from the this directory. 

Remember, you'll need to have ansible installed in your Python environment.
This can be done by "pip install ansible==1.6.3"

Here is the command that should ping your webservers:

ansible -m 'ping' webservers
