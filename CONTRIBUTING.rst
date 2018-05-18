.. _contribution_link:

============
Contributing
============

Ready to contribute? Your contributions are very much welcomed and credit will
be given. These Guidelines will help you effectively contribute to this project
and guide you to successfully merged Pull Requests.

Here's how to set up the **ansible_tutorial** for local development.


Getting Started!
----------------

This repository is in standard wheel format so it can be used like a normal Python Package. However, if you follow these instructions, you can avoid having your python environment look like this:

.. image:: https://imgs.xkcd.com/comics/python_environment.png

If you need help with background knowledge, see online training video: https://GlenJarvis.com/v/virtual-environments.

1. Find a place to work::

    $ cd path_where_you_want_this_repo

2. Clone the project::

    $ git clone https://github.com/glenjarvis/ansible_tutorial.git
    $ cd ansible_tutorial

3. Make a virtualenv named **venv** for your Python environment of choice.

    * For Python2::

        $ virtualenv venv

    * For Python3::

        $ python3 -m venv venv

4. Activate the Virtual Enviroment. Every time you come back to work on this
   project, you will need to activate your virtual environment::

       $ cd path_of_this_repo
       $ source venv/bin/activate

   When the Virtual Environment is activated, you should see ``venv`` in the
   prompt. It may look something  to this::

       (venv) $

   I often like to be able to jump to this folder quickly from
   anywhere and have it automatically setup my virtual environment.
   So, I put something like this in my ``$HOME/.bashrc`` (or equivalent)
   file:

       .. code-block:: bash

           function cd_ansible_tutorial {
               deactivate 2> /dev/null
               cd /FULL_PATH_TO_THIS_DIRECTORY
               source venv/bin/activate
           }

5. Upgrade Pip. The Pip that comes with a new Virtual Environment is often too
   old. Upgrade it to be sure it is current::

       (venv)$ pip install --upgrade pip

6. Pip install as editable. This project is in wheel format. So, simply install
   a reference in your virtual environment so that you can edit files in this
   folder and see an immediate affect in the virtual environment::

       (venv)$ pip install --editable .

7. Install extra packages for development::

       (venv)$  pip install -r requirements_dev.txt

8. Install the Git Hooks. Copy the contents of ``githooks`` into your checked
   out project's ``.git/hooks`` folder::

       (venv)$  cp githooks/* .git/hooks

   Note: ``git commit --no-verify`` bypasses Git Hooks. Please don't do that
   unless the Git Hooks are actually broken.

9. Check out a topic branch and begin working.


Linting and Style
-----------------

Before any pull request is submitted, please ensure that you follow this
project's style and linting guidelines. We supply some Git Hooks to help you
with this.

Every commit's applicable files should:

* Pass `pycodestyle <https://pypi.org/project/pycodestyle/>`__ and be `PEP8
  <https://www.python.org/dev/peps/pep-0008/>`_ compliant.

* Pass default `PyLint <https://pypi.org/project/pylint/>`__ with score of 9.0
  or above (preferrably 10.0).

  If there is something that `PyLint <https://pypi.org/project/pylint/>`__ has
  gotten wrong (not that uncommon), make it clear to both the readers of your
  your code and to `PyLint <https://pypi.org/project/pylint/>`__ that your
  choice was intentional.

  For example, in a Python based Git Hook referenced below,
  `PyLint <https://pypi.org/project/pylint/>`__ gave a warning that the
  `pre-commit` filename is not a valid Python module name.

  `PyLint <https://pypi.org/project/pylint/>`__ is correct - we wouldn't
  normally want to name our Python program files ``pre-commit``. In a normal
  circumstance, we would want to name the program file ``precommit.py`` or
  something even more intuitive.

  However, having an executable script with the name of ``pre-commit`` is a
  dependency of the Git Hook and can't be avoided. Thus, to communicate this to
  both the reader of the program and `PyLint
  <https://pypi.org/project/pylint/>`__, I made these two comments toward the
  top where it was signficant::

    # "pre-commit" filename name is a hard Git dependency
    # pylint: disable=invalid-name

  The top line explains to a human reader why we are placing this comment. And,
  the second line explains to `PyLint <https://pypi.org/project/pylint/>`__ that
  this warning can be surpressed (and not lower your score).

  Thus, a `PyLint <https://pypi.org/project/pylint/>`__ score of 10.0 (the
  highest) should be possible. Both lines should be as clear and readable to a
  human as possible.


Git Hooks
^^^^^^^^^

To enforce style and linting consistency in the project, a Git Hook has been
provided to catch style and lint issues at each commit. Installation is
described above.

The ``pre-commit`` hook gives errors and stops the commit if:

- There are **any** ``pycodestyle`` violations.
- PyLint score drops below 9.0.

As with any automation, we should have a choice. The automation should help us
enforce a good coding style and not get in our way. If this Git Hook ever get in
your way, you can bypass it by using the ``--no-verify`` option (e.g., ``git
commit --no-verify``).

If this does happen, please email me at glen@glenjarvis.com with as much
relevant informaton that you can. I will want to get that fixed as quickly as I
can.


Extra Code Style
^^^^^^^^^^^^^^^^

* Functions and methods should be as short as possible, breaking concepts into
  smaller functions/methods whenever possible.

* The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and for PyPy.
  Check https://travis-ci.org/glenjarvis/ansible_tutorial/pull_requests and make sure that the tests pass
  for all supported Python versions.

* Follow the Zen::

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


Testing Guidelines
------------------

Whenever possible, you should use Test Drive Development (TDD). If you are
unfamiliar with this code design and testing concept, here is an `introductory
video <https://www.youtube.com/watch?v=sNgmSiesOG0>`__.

At the very least, all code submitted should have test coverage.


Tips and Tricks
^^^^^^^^^^^^^^^

* TravisCI will run tests against your pull requests and catch test errors:
  https://travis-ci.org/glenjarvis/ansible_tutorial/pull_requests

* The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and for PyPy.
  Running ``tox`` locally will help catch errors across versions of Python
  and make sure that the tests pass for all supported Python versions::

      $ tox


Commit Guidelines
-----------------

All commits should follow `The seven rules of a great Git commit
<https://chris.beams.io/posts/git-commit/>`_


Pull Request Guidelines
-----------------------

Please keep a good Git hygiene in your contribution. Not everyone knows how to
use a Source Control Management system like Git properly. We're here to help.

Git Training
^^^^^^^^^^^^

I teach classes in this subject and I want to help you. I am currently making
two courses:

*  Coursera course in collaboration with a UC College campus. If the current
   date is after 31-Aug, 2018 and you still see this sentence, would you please
   send me an email at glen@glenjarvis.com to remind me to place the
   Coursera link here in these Guidelines.

*  An OnLine course "How to Contribute to Open Source Projects" at
   https://GlenJarvis.com/v/contribute-open-source. This course isn't yet
   finished. Email glen@glenjarvis.com for an early adoptor invitation.

If you don't understand all of the following, you should take one of these
courses:

* The **HEAD** pointer
* The **refs** branch pointers
* The **objects** database (where everything is stored)
* How to fork
* How to push
* How to commit
* How to rebase


Guidelines
^^^^^^^^^^

* Use a different topic branch for each topic
* Keep commits small
* Rebase topic branches (i.e., Don't merge master back into topic)
* `Use proper commit message <https://chris.beams.io/posts/git-commit/>`_


Code of Conduct
---------------

We value the participation of each member of the Open Source community and want
all contributors and consumers of this project to have an enjoyable and
fulfilling experience. Accordingly, all contributors are expected to show
respect and courtesy to other contributors and community members working within
this project.

To make clear what is expected, all communication around this project by all
contributing members (including Glen Jarvis) are required to conform to the
`Python Packaging Authority Code of Conduct
<https://www.pypa.io/en/latest/code-of-conduct/>`__.


Credits
-------

This package was created with `Cookiecutter
<https://github.com/glenjarvis/ansible_tutorial/blob/master/COOKIECUTTER_CREDIT>`_

