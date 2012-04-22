# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

version = '0.0.1'

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
    name='pyoauth2',
    version=version,
    url='https://github.com/ymotongpoo/pyoauth2',
    license='New BSD',
    author='Yoshifumi YAMAGUCHI',
    author_email='ymotongpoo@gmall.com',
    description='Simple OAuth 2.0 client library',
    long_description=__doc__,
    packages=['pyoauth2'],
    package_data={},
    install_requires=[
        'setuptools',
        'requests>=0.11.1'
        ],
    extras_require=dict(
        test=[
            'nose>=1.0.0'
            ],
        ),
    test_suite='nose.collector',
    tests_require=['nose']
)

