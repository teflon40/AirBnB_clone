#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test Base model"""

    def setUp(self):
        self.my_model = BaseModel()
        self.tmp_model = BaseModel()

    def test_instance(self):
        """Test for  instances"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attr_types(self):
        """Test the attribute types"""
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_id(self):
        """Test id attribute"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertIsInstance(self.my_model.id, str)

    def test_two_obj(self):
        """Test if two objects are the same"""
        self.assertTrue(self.my_model, self.tmp_model)

    def test_to_dict(self):
        """Test if the to_dict() worked"""
        my_dict = self.my_model.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_new_attr(self):
        """Test if newly created attribute works"""
        self.my_model.number = 100
        self.assertTrue(hasattr(self.my_model, 'number'))

    def test_save(self):
        """Test if updated_at was changed after save()"""
        update = self.my_model.updated_at
        self.my_model.save()
        new_update = self.my_model.updated_at
        self.assertNotEqual(update, new_update)

    def test_str(self):
        """Test if the string representation of BaseModel object works well"""
        my_dict = self.my_model.__dict__
        my_str = f"[BaseModel] ({self.my_model.id}) {my_dict}"
        self.assertEqual(my_str, self.my_model.__str__())

if __name__ == '__main__':
    unittest.main()
