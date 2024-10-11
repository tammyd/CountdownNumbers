import unittest
try:
    from ..countdown_game import CountdownGame
except ImportError:
    from countdown_game import CountdownGame


class TestCountdownGame(unittest.TestCase):
    def setUp(self):
        self.game = CountdownGame()

    def test_find_closest_solution_exact_match(self):
        # Test that BFS finds the exact match with a simple example
        target = 987
        numbers = [100, 75, 50, 25, 10, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)

        # Check if the solution is exactly the target
        self.assertEqual(solution, target)

    def test_find_closest_solution_min_steps(self):
        # Test that BFS finds the shortest solution
        target = 125
        numbers = [100, 50, 25, 10, 5, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)

        # Check the solution is correct
        self.assertEqual(solution, target)

        # Check the solution has a minimal number of steps (should ideally be 1 for 100 + 25)
        self.assertEqual(len(steps), 1)
        self.assertIn("100 + 25 = 125", steps)

    def test_find_closest_solution_approximation(self):
        # Test that BFS finds the closest solution when the exact match is impossible
        target = 999
        numbers = [100, 75, 50, 25, 10, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)

        # Check that the solution is close to the target
        self.assertLessEqual(abs(solution - target), 10)  # Acceptable tolerance
        self.assertTrue(len(steps) > 0)  # Ensure some steps were taken

    def test_find_closest_solution_no_operations_needed(self):
        # Test that BFS returns immediately if the target is one of the numbers
        target = 100
        numbers = [100, 50, 25, 10, 5, 1]
        solution, steps = self.game.find_closest_solution(numbers, target)

        # Check if the solution is exactly the target and no steps were needed
        self.assertEqual(solution, target)
        self.assertEqual(len(steps), 0)

    def test_find_closest_solution_large_target(self):
        # Test BFS with a large target to see if it approximates well
        target = 789
        numbers = [100, 75, 50, 25, 10, 5]
        solution, steps = self.game.find_closest_solution(numbers, target)

        # Check that the solution is close to the target
        self.assertLessEqual(abs(solution - target), 20)  # Acceptable tolerance
        self.assertTrue(len(steps) > 0)  # Ensure some steps were taken


if __name__ == "__main__":
    unittest.main()
