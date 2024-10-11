# tests/test_countdown_game.py

import unittest
from countdown_numbers.countdown_game import CountdownGame

class TestCountdownGame(unittest.TestCase):
    def setUp(self):
        self.game = CountdownGame()

    def test_add(self):
        self.assertEqual(self.game.add(7, 5), 12)
        self.assertEqual(self.game.add(0, 0), 0)
        self.assertEqual(self.game.add(-3, 3), 0)

    def test_subtract(self):
        self.assertEqual(self.game.subtract(10, 3), 7)
        self.assertEqual(self.game.subtract(3, 10), 7)
        self.assertEqual(self.game.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.game.multiply(4, 6), 24)
        self.assertEqual(self.game.multiply(0, 5), 0)
        self.assertEqual(self.game.multiply(-3, 3), -9)

    def test_divide(self):
        self.assertEqual(self.game.divide(8, 2), 4)
        self.assertEqual(self.game.divide(7, 3), None)
        self.assertEqual(self.game.divide(0, 1), 0)
        self.assertEqual(self.game.divide(5, 0), None)

    def test_generate_countdown_numbers(self):
        target, numbers = self.game.generate_countdown_numbers()
        self.assertTrue(101 <= target <= 999)
        self.assertEqual(len(numbers), 6)

if __name__ == "__main__":
    unittest.main()
