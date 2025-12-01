#!/usr/bin/env python3
"""
Day 1: Secret Entrance - Part 2
https://adventofcode.com/2025/day/1

Task: Count how many times the dial points at 0 DURING OR AFTER rotations.
- Dial has positions 0-99 (circular)
- Starts at position 50
- L = rotate left (toward lower numbers), R = rotate right (toward higher numbers)
- Wraps around (L from 0 goes to 99, R from 99 goes to 0)
- Count EVERY click that lands on 0, not just the final position
"""

import sys


def solve(rotations: list[str], debug: bool = False) -> int:
    """
    Solve Part 2: Count ALL times dial passes through 0 (during or after rotation).

    Args:
        rotations: List of rotation instructions (e.g., ['L68', 'R48', ...])
        debug: If True, print detailed trace

    Returns:
        Number of times the dial points at 0 during or after any rotation
    """
    position = 50  # Starting position
    zero_count = 0

    if debug:
        print(f"Starting at position {position}")

    for rotation in rotations:
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])  # Number of clicks

        # Count passes through 0 during this rotation
        rotation_zeros = 0

        if direction == "L":
            # For each click going left, check if we hit 0
            for i in range(1, distance + 1):
                new_pos = (position - i) % 100
                if new_pos == 0:
                    rotation_zeros += 1

            new_position = (position - distance) % 100

        else:  # direction == 'R'
            # For each click going right, check if we hit 0
            for i in range(1, distance + 1):
                new_pos = (position + i) % 100
                if new_pos == 0:
                    rotation_zeros += 1

            new_position = (position + distance) % 100

        zero_count += rotation_zeros

        if debug:
            print(
                f"{rotation}: {position} -> {new_position}, zeros during rotation: {rotation_zeros}"
            )

        position = new_position

    if debug:
        print(f"\nTotal zeros: {zero_count}")

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
    debug = "--debug" in sys.argv

    # Solve the actual puzzle
    answer = (
        solve_from_file(input_file)
        if not debug
        else solve(
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"],
            debug=True,
        )
    )

    if not debug:
        print(answer)


if __name__ == "__main__":
    main()
