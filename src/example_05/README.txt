You should now be able to execute commands on all your "webservers" at once (in
our example, it will just be the host. This command will upgrade the Operating
System packages for all of your machines.

Here is the command that should ping your webservers. Just run this command
from this directory:

ansible webservers -a 'sudo yum update -y'

Or, if you wish to see more verbose output, you can use the '-vvv' options:

ansible webservers -vvv -a 'sudo yum update -y'
