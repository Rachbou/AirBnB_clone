#!/usr/bin/python3

"""
    Defines a class TestBaseModel.
"""


from models.base_model import BaseModel
import unittest
import models
import os


class TestBaseModel(unittest.TestCase):
    """Represent a TestBaseModel."""

    def test_init_id(self):
        """Test different id per object created"""

        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_id_type(self):
        """Test the id type from BaseModel"""

        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.base_model.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File base_model.py permissions"""

        test_file = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_mod_to_dict(self):
        """Test dictionary representation in BaseModel"""

        bm1 = BaseModel()
        self.assertIsInstance(bm1.to_dict(), dict)

    def test_type_object(self):
        """Test type object of BaseModel"""

        bm1 = BaseModel()
        self.assertEqual(
            str(type(bm1)),
            "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(bm1, BaseModel)

    def test_str_representation(self):
        """Test str representation of BaseModel"""

        bm1 = BaseModel()
        str_rep = "[{:s}] ({:s}) {:s}".format(
            bm1.__class__.__name__,
            bm1.id,
            str(bm1.__dict__)
        )
        self.assertEqual(str_rep, str(bm1))


if __name__ == "__main__":
    unittest.main()
