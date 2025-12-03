#!/usr/bin/env python3
"""
Day 3: Lobby - Part 1
https://adventofcode.com/2025/day/3

Task: Find the maximum joltage from each battery bank and sum them.
Each bank is a line of digits. We need to select exactly two consecutive digits
to form a 2-digit number, and find the maximum possible value.

Example: 987654321111111
- Can pick positions 0-1: 98 (maximum)
- Can pick positions 1-2: 87
- etc.
"""

import sys


def find_max_joltage(bank: str) -> int:
    """
    Find the maximum joltage from a battery bank.

    We need to pick exactly 2 batteries (not necessarily consecutive) to form a 2-digit number.
    The order is preserved - if we pick batteries at positions i and j (where i < j),
    the joltage is int(bank[i] + bank[j]).

    Args:
        bank: String of digits representing battery joltage ratings

    Returns:
        Maximum 2-digit number that can be formed from any two batteries
    """
    max_joltage = 0

    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a 2-digit number from batteries at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage


def solve(banks: list[str]) -> int:
    """
    Find the total output joltage from all battery banks.

    Args:
        banks: List of battery bank strings (each is a line of digits)

    Returns:
        Sum of maximum joltages from all banks
    """
    total = 0

    for bank in banks:
        max_joltage = find_max_joltage(bank)
        total += max_joltage

    return total


def solve_from_file(filename: str) -> int:
    """Solve using input from a file."""
    with open(filename, "r") as f:
        banks = [line.strip() for line in f if line.strip()]
    return solve(banks)


def main():
    """Main entry point - solve puzzle."""
    # Parse command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    # Solve the actual puzzle
    answer = solve_from_file(input_file)
    print(answer)


if __name__ == "__main__":
    main()
