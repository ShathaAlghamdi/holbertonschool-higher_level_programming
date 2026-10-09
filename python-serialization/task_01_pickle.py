#!/usr/bin/env python3
"""Serialize and deserialize custom Python objects using pickle."""

import pickle


class CustomObject:
    """Represent a custom object."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, EOFError, pickle.PickleError):
            return None
