Sphinx Django Command
=====================

.. image:: https://api.travis-ci.org/ZuluPro/sphinx-django-command.svg
        :target: https://travis-ci.org/ZuluPro/sphinx-django-command

Add you Django Command's help to your documentation. Just write: ::

    .. djcommand:: myapp.management.commands.mycmd

And you'll have: ::

    Usage: manage.py mycmd [options] 

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit

Useful to keep DRY documentation between Sphinx and your command help.

Setup
=====

Install with: ::

    pip install sphinx-django-command

Be sure your Sphinx ``conf.py`` has access to the command that you want to
document, the app could be found in ``sys.path`` and ``DJANGO_SETTINGS_MODULE``
is available if necessary.

Insert ``'djcommanddoc'`` in the ``extensions`` parameter: ::

    extensions = [
      ...
      'djcommanddoc',
      ...
    ]


Tests
=====

Tests are stored in `djcommanddoc.tests` and for run them you must launch:

::

    python djcommanddoc/tests.py


To run the tests across all supported versions of Django and Python, you
can use Tox. Firstly install Tox:

::

    pip install tox

To run the tests just use the command ``tox`` in the command line.  If you
want to run the tests against just one specific test environment you can run
``tox -e <testenv>``.  For example, to run the tests with Python3.3 and
Django1.9 you would run:

::

    tox -e py3.3

The available test environments can be found in ``tox.ini``.
