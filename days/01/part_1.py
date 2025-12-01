#!/usr/bin/env python3
"""
Day 1: Secret Entrance - Part 1
https://adventofcode.com/2025/day/1

Task: Count how many times the dial points at 0 AFTER rotations.
- Dial has positions 0-99 (circular)
- Starts at position 50
- L = rotate left (toward lower numbers), R = rotate right (toward higher numbers)
- Wraps around (L from 0 goes to 99, R from 99 goes to 0)
"""

import sys


def solve(rotations: list[str]) -> int:
    """
    Solve Part 1: Count times dial ends at 0 after a rotation.

    Args:
        rotations: List of rotation instructions (e.g., ['L68', 'R48', ...])

    Returns:
        Number of times the dial points at 0 after any rotation
    """
    position = 50  # Starting position
    zero_count = 0

    for rotation in rotations:
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])  # Number of clicks

        if direction == "L":
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def solve_from_file(filename: str) -> int:
    """Solve using input from a file."""
    with open(filename, "r") as f:
        rotations = [line.strip() for line in f if line.strip()]
    return solve(rotations)


def main():
    """Main entry point - solve puzzle."""
    # Parse command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    # Solve the actual puzzle
    answer = solve_from_file(input_file)
    print(answer)


if __name__ == "__main__":
    main()
