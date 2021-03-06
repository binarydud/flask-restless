# -*- coding: utf-8; Mode: Python -*-
#
# Copyright (C) 2011 Lincoln de Sousa <lincoln@comum.org>
# Copyright 2012 Jeffrey Finkelstein <jeffrey.finkelstein@gmail.com>
#
# This file is part of Flask-Restless.
#
# Flask-Restless is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Flask-Restless is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Flask-Restless. If not, see <http://www.gnu.org/licenses/>.
"""
    Flask-Restless
    ~~~~~~~~~~~~~~

    Flask-Restless is a `Flask <http://flask.pocoo.org>`_ extension which
    facilitates the creation of ReSTful JSON APIs. It is compatible with models
    which have been defined using `FLask-SQLAlchemy
    <http://packages.python.org/Flask-SQLAlchemy>`_.

    For more information, check the World Wide Web!

      * `Documentation <http://readthedocs.org/docs/flask-restless>`_
      * `PyPI listing <http://pypi.python.org/pypi/Flask-Restless>`_
      * `Source code repository <http://github.com/jfinkels/flask-restless>`_

"""
from __future__ import with_statement

import sys
from setuptools import Command
from setuptools import setup

#: The installation requirements for Flask-Restless. ``simplejson`` is only
#: required on Python version 2.5.
requirements = ['flask>=0.7', 'flask-sqlalchemy', 'python-dateutil<2.0']
if sys.version_info < (2, 6):
    requirements.append('simplejson')


class run_coverage(Command):
    """Runs ``coverage``, the Python code coverage tool to generate a test
    coverage report.

    This command requires that `coverage.py
    <http://nedbatchelder.com/code/coverage>`_ is installed. This can be done
    by doing, for example::

        pip install coverage

    """

    #: A brief description of the command.
    description = "Generate a test coverage report."

    #: Options which can be provided by the user.
    user_options = []

    def initialize_options(self):
        """Intentionally unimplemented."""
        pass

    def finalize_options(self):
        """Intentionally unimplemented."""
        pass

    def run(self):
        """Runs coverage.py on the test suite then generates an HTML report,
        both in a subprocess.

        """
        import subprocess
        try:
            subprocess.call(['coverage', 'run', '--source=flask_restless',
                             '--branch', 'run-tests.py'])
            subprocess.call(['coverage', 'html'])
        except OSError:
            print('coverage.py not found.'
                  ' Install it with "pip install coverage".')
            sys.exit(-1)
        print('HTML coverage report generated at "htmlcov/".')


setup(
    author='Jeffrey Finkelstein',
    author_email='jeffrey.finkelstein@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={'coverage': run_coverage},
    description='A Flask extension for easy ReSTful API generation',
    download_url='http://pypi.python.org/pypi/Flask-Restless',
    install_requires=requirements,
    include_package_data=True,
    keywords=['ReST', 'API', 'Flask', 'Elixir'],
    license='GNU AGPLv3+',
    long_description=__doc__,
    name='Flask-Restless',
    platforms='any',
    packages=['flask_restless'],
    test_suite='tests.suite',
    tests_require=['unittest2'],
    url='http://github.com/jfinkels/flask-restless',
    version='0.5-dev',
    zip_safe=False
)
