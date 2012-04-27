# -*- coding: utf-8 -*-

from pyoauth2.client import FileStorage

from random import choice
from string import printable

import os.path


def filepath(filename):
    return os.path.join(os.path.dirname(__file__), filename)
test_file = filepath("test.dat")

test_credential = {
    "access_token": "ThisIsTestToken"
    }


class TestFileStorage___init__(object):
    def test_normal(self):
        filename = "dummy.dat"
        test_storage = FileStorage(filename)
        assert test_storage.filename == filename

    def test_irregular(self):
        pass


class TestFileStorage_get(object):
    def test_none(self):
        test_storage = FileStorage("dummy.dat")
        assert test_storage.get() is None

    def test_normal(self):
        test_storage = FileStorage(test_file)
        assert test_storage.get() == test_credential
        

class TestFileStorage_save(object):
    def test_none(self):
        pass

    def test_normal(self):
        pass
