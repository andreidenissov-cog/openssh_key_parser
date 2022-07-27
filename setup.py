"""
Installation script for openssh-key-parser library
"""

import os
import sys
from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 8)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of Openssh Key Parser requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

def _read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as file_name:
        return file_name.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('requirements-dev.txt') as f:
    test_required = f.read().splitlines()

def local_scheme(version):
    if version.distance and version.distance > 0:
        return '.post' + str(version.distance)
    else:
        return ''

def version_scheme(version):
    return str(version.tag)

# Directly list packages we want to be included
cs_packages = [
               'openssh_key',
               'openssh_key.cipher',
               'openssh_key.kdf_options',
               'openssh_key.key_params'
              ]

setup(
    name='openssh_key_parser',
    use_scm_version={
        "version_scheme": version_scheme,
        "local_scheme": local_scheme},
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    packages=cs_packages,
    scripts=[],
    install_requires=required,
    description='OpensshKeyParser library',
    long_description=_read('README.md'),
    author='Andrei Denissov',
    author_email='andrei.denissov@cognizant.com',
    url='https://github.com/andreidenissov-cog/openssh_key_parser',
    include_package_data=True,
    zip_safe=False
)
