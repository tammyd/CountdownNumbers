import random

class CountdownGame:
    def __init__(self):
        self.large_numbers = [25, 50, 75, 100]
        self.small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2

    def generate_countdown_numbers(self, num_large=2, num_small=4):
        # Select the large and small numbers
        selected_large = random.sample(self.large_numbers, num_large)
        selected_small = random.sample(self.small_numbers, num_small)
        numbers = selected_large + selected_small

        # Generate a random target between 101 and 999
        target = random.randint(101, 999)

        return target, numbers

    # Basic arithmetic operations
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return abs(x - y)  # Always positive on Countdown

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0 and x % y == 0:  # Ensure integer result for division
            return x // y
        return None  # Return None if division isn’t possible
