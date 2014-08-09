There are more modules than just `ping`. Some of them are incredibly powerful.
One particular module is `setup`.  Don't get confused by it's name, though.

This module doesn't change the set-up. It just retrieves the information from
the server - it retrieves what has already been setup. And, as you can see,
that can be a lot of data.

Remember, you'll need to have ansible installed in your Python environment.
This can be done by "pip install ansible==1.7.0"

Here is the command that should ping your webservers:

    ansible -m setup webservers

To get more verbose output, use the `-v` (verbose) option, which can be
specified multiple times.

Try:

    ansible -vv -m setup webservers

or:

    ansible -vvv -m setup webservers
