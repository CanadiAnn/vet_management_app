import unittest

from models.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner_1 = Owner('Ann', 'Loz', 12345123456, '15 Bread St, Midlothian, Edinburgh')
        self.owner_2 = Owner('Lulu', 'Dagenais', 23456123456, '25 Castlehill Terrace, Midlothian, Edinburgh')

    def test_owner_has_first_name(self):
        self.assertEqual('Ann', self.owner_1.first_name)
        self.assertEqual('Lulu', self.owner_2.first_name)

    def test_owner_has_last_name(self):
        self.assertEqual('Loz', self.owner_1.last_name)
        self.assertEqual('Dagenais', self.owner_2.last_name)

    def test_owner_has_phone_num(self):
        self.assertEqual(12345123456, self.owner_1.phone_num)
        self.assertEqual(23456123456, self.owner_2.phone_num)

    def test_owner_has_address(self):
        self.assertEqual('15 Bread St, Midlothian, Edinburgh', self.owner_1.address)
        self.assertEqual('25 Castlehill Terrace, Midlothian, Edinburgh', self.owner_2.address)
    


    