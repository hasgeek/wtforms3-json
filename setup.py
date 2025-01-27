"""
WTForms-JSON
------------

Adds smart json support for WTForms. Useful for when using WTForms with RESTful
APIs.
"""

import os
import re
import subprocess

from setuptools import Command, setup

HERE = os.path.dirname(os.path.abspath(__file__))


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


def get_version():
    filename = os.path.join(HERE, 'wtforms_json', '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


extras_require = {
    'test': ['pytest>=2.2.3', 'flake8>=2.4.0', 'isort>=3.9.6'],
}


setup(
    name='WTForms-JSON',
    version=get_version(),
    url='https://github.com/kvesteri/wtforms-json',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description=(
        'Adds smart json support for WTForms. Useful for when using'
        ' WTForms with RESTful APIs.'
    ),
    long_description=__doc__,
    packages=['wtforms_json'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['WTForms>=3.0', 'six>=1.3.0'],
    extras_require=extras_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
