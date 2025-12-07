#!/usr/bin/env python3
"""
Day 7: Laboratories - Part 2
https://adventofcode.com/2025/day/7

Count the number of timelines created by a quantum tachyon particle.
The particle takes BOTH left and right paths at each splitter (many-worlds interpretation).
Each unique path through the manifold represents a different timeline.
"""

import sys


def solve(data):
    """
    Count the number of timelines for a quantum tachyon particle.

    In quantum mode, a single particle takes both paths at each splitter,
    creating multiple timelines (many-worlds interpretation).

    Args:
        data: List of strings representing the manifold grid

    Returns:
        Number of distinct timelines (complete paths through the grid)
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

    # Use memoized DFS to count all possible paths through the manifold
    # Each path represents a timeline
    memo = {}

    def count_paths(row, col):
        """
        Count all possible paths from (row, col) to the bottom of the grid.

        Returns:
            Number of distinct paths from this position
        """
        # Check memo first
        if (row, col) in memo:
            return memo[(row, col)]

        # Base case: reached bottom of grid
        if row >= height:
            return 1

        # Out of bounds horizontally
        if col < 0 or col >= width:
            return 0

        cell = grid[row][col]

        if cell == "^":
            # Hit a splitter - particle takes BOTH paths
            # Count paths going left and paths going right
            left_paths = count_paths(row + 1, col - 1)
            right_paths = count_paths(row + 1, col + 1)
            result = left_paths + right_paths
        else:
            # Empty space or 'S' - particle continues straight down
            result = count_paths(row + 1, col)

        # Memoize and return
        memo[(row, col)] = result
        return result

    # Start counting from the S position
    return count_paths(0, start_col)


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
