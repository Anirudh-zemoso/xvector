import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

# Don't import quandl module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'xvector'))


install_requires = [
    'requests == 2.18.4',
    'pandas'
]

installs_for_two = [
    'pyOpenSSL',
    'ndg-httpsclient',
    'pyasn1'
]

if sys.version_info[0] < 3:
    install_requires += installs_for_two

packages = [
    'xvector'
]

setup(
    name='Xvector',
    description='Package for Xvector API access',
    keywords=['xvector', 'API', 'data'],
    long_description=long_description,
    version='0.0.1',
    author='Xvector',
    author_email='anirudh.g@zemosolabs.com',
    maintainer='Xvector Development Team',
    maintainer_email='anirudh.g@zemosolabs.com',
    url='https://github.com/Anirudh-zemoso/xvector',
    license='',
    install_requires=install_requires,
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    packages=packages
)