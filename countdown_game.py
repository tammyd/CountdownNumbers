from functools import lru_cache
import random
from itertools import combinations

class CountdownGame:
    def __init__(self):
        self.large_numbers = [25, 50, 75, 100]
        self.small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2

    def generate_countdown_numbers(self, num_large=2, num_small=4):
        selected_large = random.sample(self.large_numbers, num_large)
        selected_small = random.sample(self.small_numbers, num_small)
        numbers = selected_large + selected_small
        target = random.randint(101, 999)
        return target, numbers

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return abs(x - y)

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0 and x % y == 0:
            return x // y
        return None

    def generate_pairs(self, numbers):
        return list(combinations(numbers, 2))

    def apply_operations(self, x, y):
        results = []
        operations = []

        results.append(self.add(x, y))
        operations.append(f"{x} + {y} = {self.add(x, y)}")

        if x >= y:
            results.append(self.subtract(x, y))
            operations.append(f"{x} - {y} = {self.subtract(x, y)}")
        else:
            results.append(self.subtract(y, x))
            operations.append(f"{y} - {x} = {self.subtract(y, x)}")

        if x != 1 and y != 1:
            results.append(self.multiply(x, y))
            operations.append(f"{x} * {y} = {self.multiply(x, y)}")

        if y != 1 and self.divide(x, y) is not None:
            results.append(self.divide(x, y))
            operations.append(f"{x} / {y} = {self.divide(x, y)}")
        elif x != 1 and self.divide(y, x) is not None:
            results.append(self.divide(y, x))
            operations.append(f"{y} / {x} = {self.divide(y, x)}")

        return results, operations

    def find_closest_solution(self, numbers, target, max_depth=5, use_cache=True):
        if use_cache:
            # Use the cached helper
            best_solution, best_steps = self._find_closest_solution_cached(tuple(numbers), target, float('inf'), max_depth, 0, tuple())
        else:
            # Call the helper without caching
            best_solution, best_steps = self._find_closest_solution(tuple(numbers), target, float('inf'), max_depth, 0, tuple())
        return best_solution, best_steps

    def _find_closest_solution(self, numbers, target, best_difference, max_depth, depth, steps):
        # Non-cached version of the solution
        return self._find_closest_solution_core(numbers, target, best_difference, max_depth, depth, steps)

    @lru_cache(maxsize=1000)
    def _find_closest_solution_cached(self, numbers, target, best_difference, max_depth, depth, steps):
        # Cached version of the solution
        return self._find_closest_solution_core(numbers, target, best_difference, max_depth, depth, steps)

    def _find_closest_solution_core(self, numbers, target, best_difference, max_depth, depth, steps):
        # Core logic shared by both cached and non-cached versions
        numbers = list(numbers)
        best_solution = numbers[0] if numbers else None
        best_steps = list(steps)

        if target in numbers:
            return target, best_steps

        if len(numbers) == 1 or depth >= max_depth:
            difference = abs(numbers[0] - target)
            if difference < best_difference:
                return numbers[0], best_steps
            return best_solution, best_steps

        pairs = self.generate_pairs(numbers)

        for (x, y) in pairs:
            results, operations = self.apply_operations(x, y)

            for result, operation in zip(results, operations):
                new_steps = best_steps + [operation]
                new_numbers = [num for num in numbers if num != x and num != y]
                new_numbers.append(result)

                solution, solution_steps = (
                    self._find_closest_solution_cached(tuple(new_numbers), target, best_difference, max_depth, depth + 1, tuple(new_steps))
                    if steps
                    else self._find_closest_solution(tuple(new_numbers), target, best_difference, max_depth, depth + 1, tuple(new_steps))
                )

                if solution is not None:
                    current_difference = abs(solution - target)
                    if current_difference < best_difference:
                        best_solution, best_difference, best_steps = solution, current_difference, solution_steps

        return best_solution, best_steps
