from django.test import TestCase
from .factories import DeckFactory


class TestModels(TestCase):

    def test_Deck_creation(self):
        deck = DeckFactory()

    # assertions

    self.assertTrue(deck.name)
    self.assertEqual(type(deck.name), str)
