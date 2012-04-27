# -*- coding: utf-8 -*-

from paver.easy import *
import os
import os.path
import subprocess

project_root = os.path.abspath(os.path.dirname(__file__))

@task
def deploy():
    os.chdir(project_root)
    all()
    os.chdir(project_root)
    sh("python setup.py register")
    sh("python setup.py sdist upload")


@task
def all():
    for f in [clean, build]:
        os.chdir(project_root)
        f()
    print "All task finished"


@task
def build():
    for f in [test_all, docs]:
        os.chdir(project_root)
        f()
    print "Complete building!"


@task
def docs():
    os.chdir(os.path.join(project_root, 'docs'))
    sh("make html")


@task
def test():
    os.chdir(project_root)
    sh("py.test test")

@task
def test_all():
    os.chdir(project_root)
    sh("tox")


@task
def clean():
    """Clean up previous garbage"""
    os.chdir(os.path.join(project_root, 'docs'))
    sh("make clean")
    os.chdir(project_root)
    sh("rm -rf pyoauth2.egg-info")
