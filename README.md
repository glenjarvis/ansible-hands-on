# Successfully automating your machines in the cloud using Ansible

As we have seen with the previous talk, "Red Pill, Blue Pill Virtual Machines
and Virtual Environments"
( [GitHub](https://github.com/glenjarvis/red-pill-blue-pill) /
  [YouTube](https://www.youtube.com/watch?v=xZb3cr1JrMg) ), we can create
virtual machines in the cloud.

But, how do you "stamp" those machines differently? If you need to build a web
server, mail server, DNS server, and load balancer, each machine may have the
same base image but needs to be configured differently.

If you manually configure those machines, what happens when you suddenly have a
surge in traffic and need four more web servers? Or, what if one finds a
vulnerability in a library like Heartbleed in OpenSSL as we recently
encountered. A very safe option would be to rebuild these machines from
scratch. If they were built manually, rebuilding these machines within minutes
from scratch would be daunting, tedious and error prone.

There are several tools that have been built to fix this problem. Two of the
most popular tools ([Chef](http://www.getchef.com/) and
[Puppet](http://puppetlabs.com/puppet/what-is-puppet) ) are written in the
[Ruby](https://www.ruby-lang.org/) programming language. And, especially for
the most popular, [Chef](http://www.getchef.com/), one needs somewhat of a
familiarity with that language to use the tool.

There are two more tools that are written in [Python](https://www.python.org/)
and are growing in popularity: [Salt](http://www.saltstack.com/) and
[Ansible](http://www.ansible.com/).  [Ansible](http://www.ansible.com/)
requires the least amount of set-up (if any) and has the simplest
infrastructure (it simply uses commands over ssh like
[Fabric](http://www.fabfile.org/) does). [Ansible](http://www.ansible.com/) is
the easiest tool to get started with if you are new in the machine build
automation frameworks.

We will start with a newly built machine and obtain it's public IP address. We
will configure the `ansible_host` file with the IP address, and add/build plays
(like recipes) to gradually configure that machine so that it is a
[Django](https://www.djangoproject.com/) web server running in the cloud. When
we are finished, we should have a running machine and a recipe to easily build
a seconded machine with a few keystrokes.

P.S. If you haven't previously built an [Amazon Web
Instance](http://aws.amazon.com/), I highly recommend [watching this
video](https://www.youtube.com/watch?v=xZb3cr1JrMg) in advance of the talk.


## Bio
Glen has been a full-time Python programmer since 2007 and has worked for
companies such as IBM, UC Berkeley, Sprint, Informix, and many small start-ups.
He has also worked both in the US and in the UK and has had Bioinformatics
research published in [Nucleic Acids Research (Oxford
Journals)](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2896197/). He is a
certified DBA and has also been certified in Linux/Unix Administration.

He currently works for a start-up, [RepairPal](http://repairpal.com/) (for
accurate car repair prices) using [Ruby on Rails](http://rubyonrails.org/) and
[Ansible](http://www.ansible.com/home).  Additionally, he runs a small start
up, [Glen Jarvis, LLC](http://glenjarvis.com/), that does online technical
training and assists employees obtaining telepresence in their current work
place.

Glen is the organizer for the [Silicon Valley Python MeetUp
Group](http://www.meetup.com/silicon-valley-python/) and an active member in
the [Bay Area Python Interest Group](http://baypiggies.net/) organization.

[GitHub](https://github.com/glenjarvis/)

[Google+](https://plus.google.com/u/0/+GlenJarvis/posts)

[LinkedIn](http://www.linkedin.com/in/glenjarvis)
