#!/usr/bin/python3
"""This module contains a class Student."""


class Student:
    """Class representation of student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name: The first name of student.
            last_name: The last name of student.
            age: The age
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
                Args:
            attrs:The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
