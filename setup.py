# -*- coding: utf-8 -*-

import os

from codecs import open

# Parse the version from the module without importing
with open('polyline/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

desc = "A Python implementation of Google's Encoded Polyline Algorithm Format."

with open('README.rst', 'r') as f:
    long_desc = f.read()
with open(os.path.join('requirements', 'base.txt'), 'r') as f:
    base_reqs = f.readlines()
with open(os.path.join('requirements', 'test.txt'), 'r') as f:
    test_reqs = f.readlines()

setup(
    name='polyline',
    version=version,
    description=desc,
    long_description=long_desc,
    author='Bruno M. Custódio',
    author_email='bruno@brunomcustodio.com',
    maintainer='Frederick Jansen',
    maintainer_email='frederick.jansen@gmail.com',
    url='https://github.com/hicsail/polyline',
    packages=['polyline'],
    install_requires=base_reqs,
    tests_require=test_reqs,
    test_suite='nose.collector',
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ),
)
