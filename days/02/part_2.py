#!/usr/bin/env python3
"""
Day 2: Gift Shop - Part 2
https://adventofcode.com/2025/day/2

Task: Find all invalid product IDs in given ranges and return their sum.
An invalid product ID is a number that consists of a sequence of digits repeated AT LEAST twice.
Numbers with leading zeroes are not valid product IDs.

Examples of invalid IDs:
- 55 (5 repeated 2 times)
- 111 (1 repeated 3 times)
- 12341234 (1234 repeated 2 times)
- 123123123 (123 repeated 3 times)
- 1212121212 (12 repeated 5 times)
"""

import sys


def is_invalid_id(num: int) -> bool:
    """
    Check if a number is an invalid product ID.

    An invalid ID is one where a sequence of digits is repeated at least twice.
    Leading zeroes make it invalid (e.g., 0101 would be "01" repeated, but "01" has leading zero).

    Args:
        num: The number to check

    Returns:
        True if the number is an invalid product ID, False otherwise
    """
    num_str = str(num)
    length = len(num_str)

    # Try all possible pattern lengths from 1 to length//2
    # A pattern must repeat at least twice, so max pattern length is length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the number can be divided into this pattern length
        if length % pattern_len == 0:
            pattern = num_str[:pattern_len]

            # Check for leading zero
            if pattern[0] == "0":
                continue

            # Check if the entire string is made of this pattern repeated
            num_repetitions = length // pattern_len
            if pattern * num_repetitions == num_str and num_repetitions >= 2:
                return True

    return False


def solve(ranges: list[str]) -> int:
    """
    Find all invalid product IDs in the given ranges and return their sum.

    Args:
        ranges: List of range strings in format "start-end"

    Returns:
        Sum of all invalid product IDs
    """
    total_sum = 0

    for range_str in ranges:
        start, end = map(int, range_str.split("-"))

        # Check each number in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num

    return total_sum


def solve_from_file(filename: str) -> int:
    """Solve using input from a file."""
    with open(filename, "r") as f:
        content = f.read().strip()
        # Split by commas to get individual ranges
        ranges = [r.strip() for r in content.split(",") if r.strip()]
    return solve(ranges)


def main():
    """Main entry point - solve puzzle."""
    # Parse command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    # Solve the actual puzzle
    answer = solve_from_file(input_file)
    print(answer)


if __name__ == "__main__":
    main()
