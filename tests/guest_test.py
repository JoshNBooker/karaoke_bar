import unittest
from classes.guest import Guest
from classes.drink import Drink
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John", 100, "Bohemian Rhapsody")
        self.drink1 = Drink("Tennants", 4)
        self.room1 = Room("Red Room", 30, [self.guest1], ["Immigrant Song", "Johnny B. Goode"], 3, 100)
        self.song1 = Song("Born to Run")

    def test_pay_money(self):
        self.guest1.pay_money(4)
        self.assertEqual(96, self.guest1.wallet)
    
    def test_buy_drink(self):
        amount = self.guest1.buy_drink(self.drink1)
        self.assertEqual(4, amount)
    
    def test_rent_room(self):
        amount = self.guest1.rent_room(self.room1)
        self.assertEqual(70, self.guest1.wallet)
        self.assertEqual(30, amount)


