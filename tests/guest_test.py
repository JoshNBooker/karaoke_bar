import unittest
from classes.guest import Guest
from classes.drink import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John", 100, "Bohemian Rhapsody")
        self.drink1 = Drink("Tennants", 4)

    def test_pay_money(self):
        self.guest1.pay_money(self.drink1.price)
        self.assertEqual(96, self.guest1.wallet)

