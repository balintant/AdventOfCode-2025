#!/usr/bin/env python3
"""
Day 9: Movie Theater - Part 1
https://adventofcode.com/2025/day/9

Find the largest rectangle that can be formed using red tiles as opposite corners.
"""

import sys


def solve(data):
    """
    Find the largest rectangle area where two red tiles are opposite corners.

    Args:
        data: List of strings, each containing "x,y" coordinates of red tiles

    Returns:
        int: Maximum rectangle area
    """
    # Parse coordinates
    tiles = []
    for line in data:
        line = line.strip()
        if line:
            x, y = map(int, line.split(","))
            tiles.append((x, y))

    # Try all pairs of red tiles as opposite corners
    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            # Calculate rectangle dimensions (inclusive of both corners)
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            max_area = max(max_area, area)

    return max_area


def solve_from_file(filename):
    """Read input from file and solve the puzzle."""
    with open(filename, "r") as f:
        data = f.readlines()
    return solve(data)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
