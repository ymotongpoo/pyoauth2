# -*- coding: utf-8 -*-

from pyoauth2.client import FileStorage

class TestFileStorage___init__():
    def test_normal():
        filename = "test.dat"
        test_storage = FileStorage(filename)
        assert test_storage.filename == filename


def test_filestorage_get():
    test_storage = FileStorage()
    assert test_storage.get() is None
