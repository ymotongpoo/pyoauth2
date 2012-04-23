# -*- coding: utf-8 -*-

import sys
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

import pyoauth2

short_description = "Simple OAuth 2.0 client library"
long_description = open('README.rst', 'rb').read()

version = pyoauth2.version

classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console'
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
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
        'requests>=0.11.1'
        ],
    extras_require = dict(
        test=[
            'pytest>=2.2'
            ]
        ),
    test_suite='test.suite',
    test_require=['pytest']
    )

