try:
    from .countdown_game import CountdownGame
except ImportError:
    from countdown_game import CountdownGame


def main():
    game = CountdownGame()

    # Choose to generate numbers or input manually
    choice = input("Generate random numbers and target? (y/n): ").strip().lower()

    if choice == 'y':
        target, numbers = game.generate_countdown_numbers()
    else:
        target = int(input("Enter the target number: "))
        numbers = list(map(int, input("Enter 6 numbers separated by spaces: ").split()))

    print(f"\nTarget: {target}")
    print(f"Numbers: {numbers}")

    # Find solution and print steps
    solution, steps = game.find_closest_solution(numbers, target)
    print(f"\nClosest Solution: {solution}")
    print("Steps:")
    for step in steps:
        print(step)


if __name__ == "__main__":
    main()
