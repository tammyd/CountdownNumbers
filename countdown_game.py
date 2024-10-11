from itertools import combinations
from collections import deque

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

    def find_closest_solution(self, numbers, target):
        # BFS initialization
        queue = deque([(numbers, [], 0)])  # (current numbers, operations so far, current difference)
        visited = set()  # Track visited states to avoid repeats
        best_solution = None
        best_steps = []
        best_difference = float("inf")

        while queue:
            current_numbers, steps, current_difference = queue.popleft()

            # Check if target is directly reachable
            if target in current_numbers:
                return target, steps  # Solution found

            # Add the state to visited
            state = tuple(sorted(current_numbers))
            if state in visited:
                continue
            visited.add(state)

            # Generate pairs and apply operations to create new states
            for (x, y) in self.generate_pairs(current_numbers):
                results, operations = self.apply_operations(x, y)

                for result, operation in zip(results, operations):
                    new_numbers = [num for num in current_numbers if num != x and num != y] + [result]
                    new_steps = steps + [operation]
                    new_difference = abs(result - target)

                    # Update the best solution if this is closer
                    if new_difference < best_difference:
                        best_solution = result
                        best_steps = new_steps
                        best_difference = new_difference

                    # Add new state to the queue if it hasn't been visited
                    queue.append((new_numbers, new_steps, new_difference))

        return best_solution, best_steps
