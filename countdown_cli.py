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
        help="The target number to reach (required if --numbers is provided).",
    )
    parser.add_argument(
        "--numbers",
        type=str,
        help="A comma-separated or space-separated list of 6 numbers to use.",
    )
    parser.add_argument(
        "--big",
        type=int,
        help="Number of big numbers to use (25, 50, 75, 100). Must be non-negative.",
    )
    parser.add_argument(
        "--small",
        type=int,
        help="Number of small numbers to use (1–10). Must be non-negative.",
    )
    args = parser.parse_args()

    # Default total count of numbers in the game
    total_numbers = 6
    max_big_numbers = 4

    # Validate non-negative values for `--big` and `--small`
    if (args.big is not None and args.big < 0) or (
        args.small is not None and args.small < 0
    ):
        print("Error: --big and --small must be non-negative integers.")
        return

    # Determine the number of big and small numbers to use, with validation
    if args.big is not None and args.small is None:
        num_large = args.big
        num_small = total_numbers - num_large
    elif args.small is not None and args.big is None:
        num_small = args.small
        num_large = total_numbers - num_small
    else:
        # Use provided values or defaults if both are specified or neither is specified
        num_large = args.big if args.big is not None else 2
        num_small = args.small if args.small is not None else 4

    # Validate that the total count of big and small numbers equals six
    if num_large + num_small != total_numbers or num_large > max_big_numbers:
        print(
            f"Error: Invalid number of big or small numbers. You must choose a total of {total_numbers} numbers, with up to {max_big_numbers} big numbers."
        )
        return

    game = CountdownGame()

    # Check if the user specified enough information; otherwise, prompt
    if not args.target and not args.numbers and not args.big and not args.small:
        # Prompt for random generation if no numbers or target are specified
        choice = input("Generate random numbers and target? (y/n): ").strip().lower()
        if choice == "y":
            target, numbers = game.generate_countdown_numbers(
                num_large=num_large, num_small=num_small
            )
        else:
            # Manual entry if the user does not want random generation
            target = int(input("Enter the target number: "))
            numbers_input = input(
                "Enter 6 numbers separated by spaces or commas: "
            ).replace(",", " ")
            numbers = list(map(int, numbers_input.split()))
    elif args.target and args.numbers:
        # Use specified target and numbers directly
        target = args.target
        numbers = list(map(int, args.numbers.replace(",", " ").split()))
    else:
        # Automatically generate random numbers if --big or --small is specified
        target, numbers = game.generate_countdown_numbers(
            num_large=num_large, num_small=num_small
        )

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
