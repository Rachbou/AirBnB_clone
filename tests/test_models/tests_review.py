#!/usr/bin/python3

"""
    Defines a class Review.
"""


from models.review import Review
import unittest
import models
import os


class TestReview(unittest.TestCase):
    """Represent a Review test."""

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.review.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Review.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File review.py permissions"""

        test_file = os.access("models/review.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/review.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/review.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of Review"""

        review = Review()
        self.assertEqual(
            str(type(review)),
            "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)


if __name__ == "__main__":
    unittest.main()
