You should now be able to execute commands on all your "webservers" at once (in
our example, it will just be the host. This command will upgrade the Operating
System packages for all of your machines.

Here is the command that should ping your webservers. Just run this command
from this directory:

    ansible webservers -vvv -a 'sudo yum update -y'
