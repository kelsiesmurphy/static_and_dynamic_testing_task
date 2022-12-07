import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Hearts", 2)
        self.cards = [self.card1, self.card2]

    def test_get_suit_from_card(self):
        self.assertEqual("Clubs", self.card1.suit)

    def test_get_value_from_card(self):
        self.assertEqual(2, self.card2.value)

    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))

    def test_highest_card(self):
        self.assertEqual("Hearts", CardGame.highest_card(self, self.card1, self.card2).suit)

    def test_card_total(self):
        self.assertEqual("You have a total of3", CardGame.cards_total(self, self.cards))