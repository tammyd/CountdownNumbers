import time
import argparse

try:
    from .countdown_game import CountdownGame
except ImportError:
    from countdown_game import CountdownGame


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Solve Countdown number problems.")
    parser.add_argument(
        "--optimize",
        action="store_true",
        help="Enable caching optimizations to improve performance."
    )
    args = parser.parse_args()

    game = CountdownGame()

    # Choose to generate numbers or input manually
    choice = input("Generate random numbers and target? (y/n): ").strip().lower()

    if choice == 'y':
        target, numbers = game.generate_countdown_numbers()
    else:
        target = int(input("Enter the target number: "))
        numbers_input = input("Enter 6 numbers separated by spaces or commas: ").replace(",", " ")
        numbers = list(map(int, numbers_input.split()))

    print(f"\nTarget: {target}")
    print(f"Numbers: {numbers}")

    # Measure time to solve
    start_time = time.time()
    if args.optimize:
        # Use caching (optimized version)
        solution, steps = game.find_closest_solution(numbers, target, use_cache=True)
    else:
        # Disable caching
        solution, steps = game.find_closest_solution(numbers, target, use_cache=False)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display solution, steps, and time taken
    print(f"\nClosest Solution: {solution}")
    print("Steps:")
    for step in steps:
        print(step)
    print(f"\nTime taken: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()
