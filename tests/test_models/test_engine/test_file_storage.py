#!/usr/bin/python3

"""
    Defines a class TestFileStorage.
"""


from models.engine.file_storage import FileStorage
import unittest
import models
import os


class TestFileStorage(unittest.TestCase):
    """Represent a TestFileStorage."""

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.engine.file_storage.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(FileStorage.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File file_storage.py permissions"""

        test_file = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of FileStorage"""

        storage = FileStorage()
        self.assertEqual(
            str(type(storage)),
            "<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
