#!/usr/bin/python3
"""Unittest for base.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for base.py file"""

    def test_instance_type_id_class(self):
        """Checks for a instance of the class
        """
        print("--->Check for instance Base class, id and type")
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_none_id(self):
        """Checks when id is none
        """
        print("--->Instance with none ids")
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_id_value(self):
        """Checks when id has a integer value
        """
        print("--->Instances with custom id values")
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1.id = 4
        self.assertEqual(b1.id, 4)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)
        b2 = Base(0)
        self.assertEqual(b2.id, 0)
        b1 = Base(100e+1000)
        self.assertEqual(b1.id, 100e+1000)
        b1.__init__(30)
        self.assertEqual(b1.id, 30)

    def test_object_attributtes(self):
        """Check for attributes dictionary of a object"""
        print("--->Check for attributtes dictionary")
        b1 = Base()
        self.assertEqual(b1.__dict__, {'id': 1})
        b2 = Base()
        self.assertEqual(b2.__dict__, {'id': 2})
        b3 = Base(100)
        self.assertEqual(b3.__dict__, {'id': 100})

    def test_raise_errors(self):
        """Check for raises errors
        """
        print("--->Check for important raises errors")
        with self.assertRaises(AttributeError):
            b1 = Base()
            print(b1.x)
        with self.assertRaises(NameError):
            b1 = Base_geometry()
        with self.assertRaises(AttributeError):
            b1.to_dictionary()

    def test_JSON_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = (r1.to_dictionary())
        json_dictionary = Base.to_json_string([(dictionary)])
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r2 = Rectangle(10, 7, 2, 8, 30)
        dictionary = r2.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 30, "height": 7, "width": 10}]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r3 = Rectangle(30, 50)
        dictionary = r3.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 0, "y": 0, "id": 2, "height": 50, "width": 30}]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r4 = Rectangle(30, 50, 0, 0)
        dictionary = r4.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 0, "y": 0, "id": 3, "height": 50, "width": 30}]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        r5 = Rectangle(30, 50, 0, 0, 89)
        dictionary = r5.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 0, "y": 0, "id": 89, "height": 50, "width": 30}]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

    # def test_save_to_file(self):
    #     r1 = Rectangle(10, 7, 2, 8)
    #     r2 = Rectangle(2, 4)
    #     Rectangle.save_to_file([r1, r2])
    #     with open("Rectangle.json", "r") as file:
    #         self.assertEqual(file.read(), [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])

    def test_from_json_string(self):
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89, 'x': 3, 'y': 2}, {'height': 7, 'width': 1, 'id': 7, 'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89, 'x': 3, 'y': 2}, {'height': 7, 'width': 1, 'id': 7, 'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)


    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        print(r2)
        print(r1 is r2)
        print(r1 == r2)

    def tearDown(self):
        """Tear down test method
        """
        print("Tear down - Reset nb_object attribute to zero")
        Base._Base__nb_objects = 0

if __name__ == '__main__':
    unittest.main()
