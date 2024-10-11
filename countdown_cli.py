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
        "--target",
        type=int,
        help="The target number to reach (required if --numbers is provided)."
    )
    parser.add_argument(
        "--numbers",
        type=str,
        help="A comma-separated or space-separated list of 6 numbers to use."
    )
    args = parser.parse_args()

    game = CountdownGame()

    # Determine target and numbers based on provided arguments or user input
    if args.target and args.numbers:
        target = args.target
        numbers = list(map(int, args.numbers.replace(",", " ").split()))
    else:
        # Fallback to interactive input if no command-line arguments provided
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
    solution, steps = game.find_closest_solution(numbers, target)
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
