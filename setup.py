# -*- coding: utf-8 -*-

import sys
import os.path
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

def read_file(name):
    path = os.path.join(os.path.dirname(__file__), name)
    f = open(os.path.abspath(path), 'r')
    data = f.read()
    f.close()
    return data

short_description = "Simple OAuth 2.0 client library"

try:
    long_description = read_file('README.rst'),
except IOError:
    long_description = ""

version = '0.0.4'

classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console'
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries'
        'Topic :: Utilities',
    ]

setup(
    name="pyoauth2",
    version=version,
    url=r"https://github.com/ymotongpoo/pyoauth2",
    license='New BSD',
    author="Yoshifumi YAMAGUCHI",
    author_email="ymotongpoo at gmall.com",
    description=short_description,
    long_description=long_description,
    packages=['pyoauth2'],
    package_data={},
    install_requires=[
        'setuptools',
        'requests>=0.11.1',
        ],
    extras_require = dict(
        test=[
            'pytest>=2.2',
            'coverage>=3.5',
            'mock>=0.8.0'
            ]
        ),
    test_suite='test.suite',
    test_require=['pytest']
    )

