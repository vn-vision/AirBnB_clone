#!/usr/bin/python3
''' This script ensures all objects are working as expected '''

import unittest
from models.base_model import BaseModel
from models.place import Place  # Added import statement for Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models import storage
from console import HBNBCommand
from io import StringIO
import sys
import os
from datetime import datetime


class TestModels(unittest.TestCase):
    ''' class to test all models in this project '''

    def setUp(self):
        ''' setting up variables  attributes '''
        self.console = HBNBCommand()
        self.base_model = BaseModel()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.review = Review()
        self.amenity = Amenity()
        self.user = User()

    def test_base_model(self):
        ''' this is the BaseModel '''
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_place(self):
        ''' Testing Place class attributes '''
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, float)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_state(self):
        ''' Testing State class attributes '''
        self.assertIsInstance(self.state.name, str)

    def test_city(self):
        ''' Testing City class attributes '''
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_review(self):
        ''' Testing Review class attributes '''
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_amenity(self):
        ''' Testing Amenity class attributes '''
        self.assertIsInstance(self.amenity.name, str)

    def test_user(self):
        ''' Testing User class attributes '''
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_console_create(self):
        ''' tests for Console Create Command'''
        with StringIO() as out:
            sys.stdout = out
            self.console.onecmd("create BaseModel")
            sys.stdout = sys.__stdout__
            output = out.getvalue().strip()
            self.assertTrue(output != "")

    def test_console_show(self):
        ''' Console show '''
        with StringIO() as out:
            sys.stdout = out
            self.console.onecmd("show BaseModel 1234-5678")
            sys.stdout = sys.__stdout__
            output = out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_console_destroy(self):
        ''' Console Destroy Command '''
        with StringIO() as out:
            sys.stdout = out
            self.console.onecmd("destroy BaseModel 1234-5678")
            sys.stdout = sys.__stdout__
            output = out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_console_all(self):
        ''' Console all '''
        with StringIO() as out:
            sys.stdout = out
            self.console.onecmd("all")
            sys.stdout = sys.__stdout__
            output = out.getvalue().strip()
            self.assertTrue(output != "")

    def test_console_update(self):
        ''' Console Update Command '''
        with StringIO() as out:
            sys.stdout = out
            self.console.onecmd("update BaseModel 1234-5678 attribute value")
            sys.stdout = sys.__stdout__
            output = out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_storage_new(self):
        ''' create new objects '''
        storage.new(self.base_model)
        self.assertIn("BaseModel." + self.base_model.id, storage.all())

    def test_storage_save(self):
        ''' save in storage '''
        storage.new(self.base_model)
        storage.new(self.place)
        storage.save()

        with open("file.json", "r") as f:
            data = f.read()
            self.assertIn("BaseModel." + self.base_model.id, data)
            self.assertIn("Place." + self.place.id, data)

        os.remove("file.json")

    def test_storage_reload(self):
        ''' reload from storage '''
        storage.new(self.state)
        storage.new(self.city)
        storage.save()
        storage.reload()

        self.assertIn("State." + self.state.id, storage.all())
        self.assertIn("City." + self.city.id, storage.all())


if __name__ == '__main__':
    unittest.main()
