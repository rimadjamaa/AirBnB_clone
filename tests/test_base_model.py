import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        # Add more assertions as needed

    def test_attributes(self):
        obj = BaseModel()
        obj.name = "Test"
        self.assertEqual(obj.name, "Test")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
