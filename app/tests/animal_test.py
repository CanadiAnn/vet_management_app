import unittest

from models.animal import Animal

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal_1 = Animal('Boubou', 'August 4, 2008', 'cat', 'Ann')
        self.animal_2 = Animal('Ti-Gars', 'November 17, 2012', 'fat cat', 'Lulu')

    def test_animal_has_name(self):
        self.assertEqual('Boubou', self.animal_1.name)
        self.assertEqual('Ti-Gars', self.animal_2.name)

    def test_animal_has_dob(self):    
        self.assertEqual('August 4, 2008', self.animal_1.dob)
        self.assertEqual('November 17, 2012', self.animal_2.dob)

    def test_animal_has_type(self):
        self.assertEqual('cat', self.animal_1.type)
        self.assertEqual('fat cat', self.animal_2.type)

    def test_animal_has_owner(self):
        self.assertEqual('Ann', self.animal_1.owner_id)
        self.assertEqual('Lulu', self.animal_2.owner_id)

    



    
