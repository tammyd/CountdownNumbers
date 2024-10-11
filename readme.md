# Countdown Numbers Game Solver

A Python project that solves the Countdown numbers game, allowing users to find the shortest sequence of operations to reach a target number using a specified set of numbers. The project includes a CLI interface for direct play and an underlying class (`CountdownGame`) with methods for random number generation and solution computation.

## Project Structure

```
countdown_numbers/
├── countdown_game.py         # Core logic for solving the game
├── countdown_cli.py          # Command-line interface
└── tests/
    ├── test_countdown_game.py # Unit tests for CountdownGame
    └── __init__.py
```

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. (Optional) Create and activate a virtual environment.
4. Install `pytest` for testing.

```bash
pip install pytest
```

## Usage

### Command-Line Interface

You can use the CLI to solve Countdown problems by specifying the target number and six numbers or letting it generate them randomly:

```bash
python countdown_cli.py --target 789 --numbers "100, 75, 50, 25, 10, 1"
```

Alternatively, generate random numbers with a custom split of big and small numbers:

```bash
python countdown_cli.py --big 2 --small 4
```

### Arguments

- `--target`: Specify a target number to reach.
- `--numbers`: Provide a comma- or space-separated list of six numbers.
- `--big` and `--small`: Define the count of big and small numbers for random generation.

## Running Tests

To run the tests for `CountdownGame`, use:

```bash
pytest tests/test_countdown_game.py
```

This command will execute the tests and confirm the accuracy and reliability of the game logic.

## Human Disclaimer

Not gonna lie, I used ChatGPT 4o to do the heavy lifting here. It did take a fair amount of back and forth to get 
things to where I was happy with them, but this would have taken me considerably longer without ChatGPT. 