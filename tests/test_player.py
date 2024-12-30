import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Player1")

    def test_add_resources(self):
        self.player.add_resources("money", 10)
        self.assertEqual(self.player.resources["money"], 10)

    def test_remove_resources(self):
        self.player.add_resources("money", 10)
        self.player.remove_resources("money", 5)
        self.assertEqual(self.player.resources["money"], 5)

    def test_add_card(self):
        card = "Card1"
        self.player.add_card(card)
        self.assertIn(card, self.player.cards)

    def test_play_card(self):
        card = "Card1"
        self.player.add_card(card)
        self.player.play_card(card)
        self.assertNotIn(card, self.player.cards)

    def test_add_action(self):
        action = "Action1"
        self.player.add_action(action)
        self.assertIn(action, self.player.actions)

    def test_perform_action(self):
        action = "Action1"
        self.player.add_action(action)
        self.player.perform_action(action)
        self.assertNotIn(action, self.player.actions)

    def test_update_player_state(self):
        # Add code to test the update_player_state method
        pass

if __name__ == '__main__':
    unittest.main()
