#!/usr/bin/env python3
"""
Testing module for the BaseModel Class
"""
import unittest
import models.base_model as base
import datetime
import uuid
BaseModel = base.BaseModel


class TestBaseClass(unittest.TestCase):
    """
    TestBaseClass: - : A class to test my BaseModel class
    """
    def setUp(self):
        """
        Sets up all values for each test case
        """
        self.my_model = BaseModel()
        self.my_model.number = 89
        self.my_model.name = "Fancy_Model"

    def tearDown(self):
        """
        removes all memory allocated or variables
        declared after each test
        """
        self.my_model = None

    def test_attr_type(self):
        """
        test if my instances attributes have the correct types
        """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsNotNone(self.my_model.id)

    def test_output(self):
        """
        test if my instances have the correct output
        """
        class_name = self.my_model.__class__.__name__
        inst_id = self.my_model.id
        inst_dict = self.my_model.__dict__
        test = f"[{class_name}] ({inst_id}) {inst_dict}"
        self.assertEqual(self.my_model.__str__(), test)

    def test_id(self):
        """
        tests the id of created instances
        """
        id2 = BaseModel().id
        try:
            uuid_obj = uuid.UUID(self.my_model.id)
            uuid_obj = True
        except ValueError:
            uuid_obj = False
        self.assertTrue(uuid_obj)
        self.assertNotEqual(self.my_model.id, id2)

    def test_time_value(self):
        """tests the value of created_at and updated_at of my
        instance
        """
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.assertIsNotNone(self.my_model.created_at)
        self.assertIsNotNone(self.my_model.updated_at)

    def test_save_method(self):
        """
        tests the save method in the BaseModel class
        """
        prev_updated_time = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, prev_updated_time)

    def test_time_is_string(self):
        """
        tests if created_at and updated_at were converted to
        strings in the value returned by to_dict
        """
        self.assertIsInstance(self.my_model.to_dict()["created_at"], str)
        self.assertIsInstance(self.my_model.to_dict()["updated_at"], str)

    def test_documentations(self):
        """
        checks if all documentation are given
        """
        self.assertIsNotNone(base.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instance_clone(self):
        """
        checks if i successfully created a new instance
        from the dictionary representation of a former instance
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        # ----- Assertions -----
        self.assertIsNotNone(new_model)
        self.test_attr_type()

    def test_instance_clone_instance_type(self):
        """
        checks if after the cloning from a dictionary object,
        my created_at and updated_at string are converted to
        a datetime instance
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        # ----- Assertions -----
        self.assertIsInstance(new_model, BaseModel)
        self.assertIsInstance(new_model.number, int)
        self.assertIsInstance(new_model.name, str)
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)

    def test_instance_clone_time_change(self):
        """
        checks if a new time is created after cloning or it uses
        the time from the dict object
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        self.assertEqual(self.my_model.created_at, new_model.created_at)
        self.assertEqual(self.my_model.updated_at, new_model.updated_at)

    def test_instance_clone_id(self):
        """
        checks if the cloned instances are the same
        by id
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        self.assertNotEqual(id(self.my_model), id(new_model))

    def test_instance_clone_same(self):
        """
        checks if the instance and the instance clone are the
        same using the is operator
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        self.assertFalse(self.my_model is new_model)


if __name__ == '__main__':
    unittest.main()
