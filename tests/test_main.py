import unittest
from main import initialize_game, main_game_loop

class TestMain(unittest.TestCase):

    def test_initialize_game(self):
        # Add code to test the game initialization function
        self.assertTrue(initialize_game())

    def test_main_game_loop(self):
        # Add code to test the main game loop function
        self.assertTrue(main_game_loop())

if __name__ == '__main__':
    unittest.main()
