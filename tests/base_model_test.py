#!/usr/bin/env python3
""" test for BaseModel """


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """BaseModel unittest defination """

    def test_ready(self):
        """ setup for tests """
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id_type(self):
        """ id type testing """
        self.assertEqual(type(self.model.id), str)

    def test_created_type(self):
        """ created at type test """
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_type(self):
        """ updated at type test """
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_name_type(self):
        """ name type test """
        self.assertEqual(type(self.model.name), str)

    def tset_number_type(self):
        """ number type test """
        self.assertEqual(type(self.model.my_number), int)

    def test_save_updates(self):
        """ save updated test """
        last = self.model.updated_at
        self.model.save()
        self.assertNotEqual(last, self.model.updated_at)

    def  test_returns_dict(self):
        """ dict return type test """
        self.assertEqual(type(self.model.to_dict()), dict)

    def test_correct_keys(self):
        """ dict have containing correct keys test """
        mo = self.model.to_dict()
        self.assertIn('id', mo)
        self.assertIn('created_at', mo)
        self.assertIn('updated_at', mo)
        self.assertIn('name', mo)
        self.assertIn('my_number', mo)
        self.assertIn('__class__', mo)

    def test_created_at_format(self):
        """ created at format test """
        mo = self.model.to_dict()
        created_at = mo['created_at']
        self.assertEqual(created_at, self.model.created_at.isoformat())

    def test_updated_at_format(self):
        """ updated at format test """
        mo = self.model.to_dict()
        updated_at = mo['updated_at']
        self.assertEqual(updated_at, self.model.updated_at.isoformat())


class TestBaseModelTwo(unittest.TestCase):


    def test_ready(self):
        """ setup for tests two """
        self.my_model = BaseModel()

    def test_generation_for_id(self):
        """ test for id type of generation """
        self.assertIsInstance(self.my_model.id, str)

    def test_representation_of_str(self):
        """ test for str representation """
        want = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), want)

    def test_method(self):
        """ dict method test """
        own_mo = self.my_model.to_dict()
        self.assertIsInstance(own_mo['created_at'], str)
        self.assertIsInstance(own_mo['updated_at'], str)
        self.assertEqual(own_mo['__class__'], 'BaseModel')

    def test_dict_method_from_test(self):
        """ dict method from test """
        own_mo = self.my_model.to_dict()
        own_fashoin_mo = BaseModel(**own_mo)
        self.assertIsInstance(own_fashoin_mo, BaseModel)
        self.assertEqual(own_fashoin_mo.id, self.my_model.id)
        self.assertEqual(own_fashoin_mo.created_at, self.my_model.created_at)
        self.assertEqual(own_fashoin_mo.updated_at, self.my_model.updated_at)

    def test_created_at_and_updated_at_types_both(self):
        """ created at and updated at types testing """
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)


class TestBaseModelThree(unittest.TestCase):
    """ model three unittest defination """

    def test_state_1(self):
        """ state test """
        pos = State()
        pos.name = "Kenya"
        self.assertEqual(pos.name, "Kenya")

    def test_city_2(self):
        """ city test """
        s_id = uuid4()
        c = City()
        c.name = "Nairobi"
        c.s_id = s_id
        self.assertEqual(c.name, "Nairobi")
        self.assertEqual(c.s_id, s_id)

    def test_amenity_3(self):
        """ amenity test """
        amen = Amenity()
        amen.name = "Free Wifi"
        self.assertEqual(amen.name, "Free Wifi")

    def test_review_4(self):
        """ review test """
        p_id = uuid4()
        u_id = uuid4()
        rev = Review()
        rev.p_id = p_id
        rev.u_id = u_id
        rev.text = "Good"
        self.assertEqual(rev.p_id, place_id)
        self.assertEqual(rev.u_id, user_id)
        self.assertEqual(rev.text, "Good")


if __name__ == "__main__":
    unittest.main()
