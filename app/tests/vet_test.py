import unittest

from models.vet import Vet
from models.animal import Animal

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet_1 = Vet('Kate', 'Bees', 10004567)
        self.vet_2 = Vet('Alex', 'Padmore', 10009876)
        
    def test_vet_has_first_name(self):
        self.assertEqual('Kate',self.vet_1.first_name)
        self.assertEqual('Alex',self.vet_2.first_name)

    def test_vet_has_last_name(self):    
        self.assertEqual('Bees',self.vet_1.last_name)
        self.assertEqual('Padmore',self.vet_2.last_name)

    def test_vet_has_license(self):    
        self.assertEqual(10004567,self.vet_1.license)
        self.assertEqual(10009876,self.vet_2.license)

    def test_add_animal_under_care(self):
        animal = Animal('Brasco', 'March 23, 2015', 'dog', 'Vanessa')
        self.assertEqual('Brasco', animal.name)    

