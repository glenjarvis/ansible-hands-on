You should now be able to execute commands on all your "demoserver" at once (in
our example, it will just be the host. This command will upgrade the Operating
System packages for all of your machines.

Here is the command that should ping your demoserver. Just run this command
from this directory:

ansible demoserver -a 'sudo yum update -y'

To get more verbose output, use the `-v` (verbose) option, which can be
specified multiple times.

Try:

    ansible demoserver -vv -a 'sudo yum update -y'

or:

    ansible demoserver -vvv -a 'sudo yum update -y'
