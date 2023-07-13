import unittest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Red room", 30, ["John", "Mary"], ["Pretty Woman"], 5, 100)
        self.song1 = Song("Bohemian Rhapsody")
        self.guest1 = Guest("Frank", 100, "Hero")
        self.drink1 = Drink("Tequila", 3.00)
    
    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1.name)
        self.assertEqual(["John", "Mary", "Frank"], self.room1.guests)

    def test_sell_drink(self):
        amount = self.room1.sell_drink(self.guest1, self.drink1)
        self.assertEqual(103, amount)
    
    def test_add_song_to_playlist(self):
        self.room1.add_song(self.song1)
        self.assertEqual(["Pretty Woman", "Bohemian Rhapsody"], self.room1.songs)


