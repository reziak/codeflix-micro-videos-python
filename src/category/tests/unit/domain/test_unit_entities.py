import unittest
from dataclasses import is_dataclass
from datetime import datetime
from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))


    def test_constructor(self):
        category = Category(name='valid')
        self.assertEqual(category.name, 'valid')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)
        
        created_at = datetime.now()
        category = Category(
            name='valid',
            description='valid description',
            is_active=False,
            created_at=created_at
        )
        self.assertEqual(category.name, 'valid')
        self.assertEqual(category.description, 'valid description')
        self.assertEqual(category.is_active, False)
        self.assertEqual(category.created_at, created_at)
    

    def test_if_created_at_is_generated_in_constructor(self):
        c1 = Category(name='valid a')
        c2 = Category(name='valid b')
        self.assertNotEqual(
            c1.created_at.timestamp(), 
            c2.created_at.timestamp()
        )
