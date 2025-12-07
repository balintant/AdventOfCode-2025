#!/usr/bin/env python3
"""
Day 7: Laboratories - Part 1
https://adventofcode.com/2025/day/7

Count the number of times a tachyon beam is split in a manifold.
The beam starts at 'S', moves downward, and splits when hitting '^' splitters.
Each split creates two new beams (left and right) that continue downward.
"""

import sys


def solve(data):
    """
    Count the number of beam splits in the tachyon manifold.

    Args:
        data: List of strings representing the manifold grid

    Returns:
        Number of times the beam is split
    """
    grid = [line for line in data]
    height = len(grid)
    width = len(grid[0]) if grid else 0

    # Find starting position 'S'
    start_col = None
    for col in range(width):
        if grid[0][col] == "S":
            start_col = col
            break

    if start_col is None:
        return 0

    # Track active beam positions (set of column indices for each row)
    # Start with one beam at the S position
    active_beams = {start_col}
    split_count = 0

    # Process each row from top to bottom
    for row in range(1, height):
        next_beams = set()

        for col in active_beams:
            # Beam continues downward to this row
            if col < 0 or col >= width:
                continue

            cell = grid[row][col]

            if cell == "^":
                # Hit a splitter - increment count and create two new beams
                split_count += 1
                # Left beam
                if col - 1 >= 0:
                    next_beams.add(col - 1)
                # Right beam
                if col + 1 < width:
                    next_beams.add(col + 1)
            else:
                # Empty space - beam continues straight down
                next_beams.add(col)

        active_beams = next_beams

    return split_count


def solve_from_file(filename):
    """Read input from file and solve the puzzle."""
    with open(filename, "r") as f:
        data = [line.rstrip("\n") for line in f]
    return solve(data)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
