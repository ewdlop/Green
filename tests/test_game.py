import unittest
from game import GameState

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.game_state = GameState()

    def test_add_player(self):
        self.game_state.add_player("Player1")
        self.assertEqual(len(self.game_state.players), 1)
        self.assertEqual(self.game_state.players[0], "Player1")

    def test_set_board(self):
        board = "Board1"
        self.game_state.set_board(board)
        self.assertEqual(self.game_state.board, board)

    def test_next_turn(self):
        self.game_state.add_player("Player1")
        self.game_state.add_player("Player2")
        self.game_state.next_turn()
        self.assertEqual(self.game_state.current_turn, 1)
        self.game_state.next_turn()
        self.assertEqual(self.game_state.current_turn, 0)

    def test_update_game_state(self):
        # Add code to test the update_game_state method
        pass

    def test_handle_action(self):
        # Add code to test the handle_action method
        pass

if __name__ == '__main__':
    unittest.main()
