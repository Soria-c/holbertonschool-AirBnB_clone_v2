#!/usr/bin/python3
"""Module that describe the BDStorage test class"""
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import DBStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
import MySQLdb
import mysql.connector

class TestDBStorage(unittest.TestCase):
    """Class for test the BaseModel Class method and atributes"""
    def setUp(self):
        """All variables that we need"""
        self.dbstorage = DBStorage()

    def test_dbstorage_all(self):
        self.assertTrue(type(self.dbstorage.all() is dict))

    def test_dbstorage_new(self):
        """ sets in __objects the obj with key <obj class name>.id"""
       state = State()
       state.name = "California"
       dbstorage.new()
       self.assertTrue(type(state.id) is str)

    def test_dbstorage_reload(self):
        """Create all tablexists
        ; otherwise, do nothing. If the file doesn’t exist"""
        pass

    def tearDown(self):
        """Closing the test class and deleteing the instance
            created for testing"""
        pass


if __name__ == '__main__':
    unittest.main()
