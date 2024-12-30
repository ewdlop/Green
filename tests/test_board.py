import unittest
from board import GameBoard

class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()

    def test_add_tile(self):
        tile = "Tile1"
        self.board.add_tile(tile)
        self.assertIn(tile, self.board.tiles)

    def test_update_oceans(self):
        self.board.update_oceans(1)
        self.assertEqual(self.board.oceans, 1)

    def test_update_temperature(self):
        self.board.update_temperature(2)
        self.assertEqual(self.board.temperature, -28)

    def test_update_oxygen(self):
        self.board.update_oxygen(3)
        self.assertEqual(self.board.oxygen, 3)

    def test_get_board_state(self):
        state = self.board.get_board_state()
        self.assertEqual(state["tiles"], [])
        self.assertEqual(state["oceans"], 0)
        self.assertEqual(state["temperature"], -30)
        self.assertEqual(state["oxygen"], 0)

if __name__ == '__main__':
    unittest.main()
