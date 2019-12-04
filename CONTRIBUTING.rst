.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/glenjarvis/ansible_hands_on_training/issues.

If you are reporting a bug, please include:

* Your operating system name and version (both locally and on remote hosts).
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything with labels "bug" and "help
wanted" is open to whoever wants to implement it.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/glenjarvis/ansible_hands_on_training/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `ansible_hands_on_training` for local development.

1. Fork the `ansible_hands_on_training` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:<your_github_account_name>/ansible_hands_on_training.git

3. Install your local copy into a virtualenv. Assuming you have pipenv installed, this is how you set up your fork for local development::

    $ cd ansible_hands_on_training/
    $ pipenv install --dev
    $ pip install -e .

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 ansible_hands_on_training tests
    $ python setup.py test or pytest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub. Use issue number in each commit (Issue 10 in example below)::

    $ git add .
    $ git commit -m "[Fixes 10] Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6 and 3.7, 3.8, and for PyPy.
   Check https://travis-ci.org/glenjarvis/ansible_hands_on_training/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python -m unittest tests.test_ansible_hands_on_training

