# -*- coding: utf-8 -*-

from pyoauth2.client import FileStorage

def test_filestorage___init__():
    filename = "test.dat"
    test_storage = FileStorage(filename)
    assert test_storage.filename == filename
