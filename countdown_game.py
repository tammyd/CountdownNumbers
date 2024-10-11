from itertools import combinations
from collections import deque
import random


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

    def apply_operations(self, x, y, current_numbers):
        results = []
        operations = []

        # Addition
        sum_result = self.add(x, y)
        if sum_result not in current_numbers:
            results.append(sum_result)
            operations.append(f"{x} + {y} = {sum_result}")

        # Subtraction
        if x >= y:
            diff_result = self.subtract(x, y)
            if diff_result not in current_numbers:
                results.append(diff_result)
                operations.append(f"{x} - {y} = {diff_result}")
        else:
            diff_result = self.subtract(y, x)
            if diff_result not in current_numbers:
                results.append(diff_result)
                operations.append(f"{y} - {x} = {diff_result}")

        # Multiplication (skip if either number is 1)
        if x != 1 and y != 1:
            product_result = self.multiply(x, y)
            if product_result not in current_numbers:
                results.append(product_result)
                operations.append(f"{x} * {y} = {product_result}")

        # Division (skip if division isn’t exact or if either number is 1)
        if y != 1 and self.divide(x, y) is not None:
            div_result = self.divide(x, y)
            if div_result not in current_numbers:
                results.append(div_result)
                operations.append(f"{x} / {y} = {div_result}")
        elif x != 1 and self.divide(y, x) is not None:
            div_result = self.divide(y, x)
            if div_result not in current_numbers:
                results.append(div_result)
                operations.append(f"{y} / {x} = {div_result}")

        return results, operations

    def find_closest_solution(self, numbers, target):
        queue = deque(
            [(numbers, [], 0)]
        )  # Queue of (current numbers, operations so far, current difference)
        visited = set()  # Track visited states to avoid repeats
        best_solution = None
        best_steps = []
        best_difference = float("inf")

        while queue:
            # Get the current state from the front of the queue
            current_numbers, steps, current_difference = queue.popleft()

            # If the target is in the current numbers, return it immediately as the solution
            if target in current_numbers:
                return target, steps

            # Track the state to avoid re-processing it
            state = tuple(sorted(current_numbers))
            if state in visited:
                continue
            visited.add(state)

            # Generate pairs and apply operations to create new states
            for x, y in self.generate_pairs(current_numbers):
                # Pass `current_numbers` to apply_operations to limit redundant operations
                results, operations = self.apply_operations(x, y, current_numbers)

                # For each operation result, create a new state and add it to the queue
                for result, operation in zip(results, operations):
                    new_numbers = [
                        num for num in current_numbers if num != x and num != y
                    ] + [result]
                    new_steps = steps + [operation]
                    new_difference = abs(result - target)

                    # Update the best solution if this is closer
                    if new_difference < best_difference:
                        best_solution = result
                        best_steps = new_steps
                        best_difference = new_difference

                    # Add the new state to the queue
                    queue.append((new_numbers, new_steps, new_difference))

        return best_solution, best_steps
