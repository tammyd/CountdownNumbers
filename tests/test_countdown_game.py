import unittest
from ..countdown_game import CountdownGame


class TestCountdownGame(unittest.TestCase):
    def setUp(self):
        self.game = CountdownGame()

    def test_exact_match(self):
        """Test an exact match with given target and numbers."""
        target = 125
        numbers = [100, 50, 25, 10, 5, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)
        self.assertEqual(solution, target)
        self.assertIn("100 + 25 = 125", steps)

    def test_approximate_solution(self):
        """Test finding the closest approximation when exact match is not possible."""
        target = 999
        numbers = [100, 75, 50, 25, 10, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)
        # Ensure that the solution is close to the target
        self.assertLessEqual(abs(solution - target), 10)
        self.assertTrue(len(steps) > 0)

    def test_target_in_numbers(self):
        """Test if the target is one of the numbers already."""
        target = 100
        numbers = [100, 50, 25, 10, 5, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)
        self.assertEqual(solution, target)
        self.assertEqual(len(steps), 0)  # No operations should be needed

    def test_all_small_numbers(self):
        """Test generating a solution with all small numbers."""
        target, numbers = self.game.generate_countdown_numbers(num_large=0, num_small=6)
        solution, steps = self.game.find_closest_solution(numbers, target)
        self.assertEqual(len(numbers), 6)
        self.assertTrue(all(num <= 10 for num in numbers))

    def test_all_big_numbers(self):
        """Test generating a solution with all big numbers."""
        target, numbers = self.game.generate_countdown_numbers(num_large=4, num_small=2)
        solution, steps = self.game.find_closest_solution(numbers, target)
        self.assertEqual(len(numbers), 6)
        self.assertTrue(all(num in [25, 50, 75, 100] for num in numbers[:4]))

    def test_generate_mixed_numbers(self):
        """Test generating a solution with mixed big and small numbers."""
        target, numbers = self.game.generate_countdown_numbers(num_large=2, num_small=4)
        solution, steps = self.game.find_closest_solution(numbers, target)
        self.assertEqual(len(numbers), 6)
        big_count = sum(1 for num in numbers if num in [25, 50, 75, 100])
        small_count = len(numbers) - big_count
        self.assertEqual(big_count, 2)
        self.assertEqual(small_count, 4)

    def test_closest_approximation_with_large_target(self):
        """Test finding the closest solution for a large target number."""
        target = 789
        numbers = [100, 75, 50, 25, 10, 5]
        solution, steps = self.game.find_closest_solution(numbers, target)
        self.assertLessEqual(abs(solution - target), 20)

    def test_division_not_in_current_numbers(self):
        """Test a division operation where the result is not in current numbers and y != 1."""
        x, y = 10, 2
        current_numbers = [10, 2, 5]  # Ensure the division result (5) is not added again

        results, operations = self.game.apply_operations(x, y, current_numbers)

        # Check that division was skipped because 5 already exists in current_numbers
        self.assertNotIn("10 / 2 = 5", operations)


if __name__ == "__main__":
    unittest.main()
