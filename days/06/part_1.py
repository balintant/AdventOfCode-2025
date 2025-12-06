#!/usr/bin/env python3
"""
Day 6: Trash Compactor - Part 1
https://adventofcode.com/2025/day/6

Parse vertically-oriented math problems and calculate the grand total.
Each operator represents one problem.
"""

import sys


def solve(data):
    """
    Solve the trash compactor math worksheet problem.

    Parse column values on-the-fly as we process each operator.

    Args:
        data: List of strings representing the worksheet rows

    Returns:
        The grand total (sum of all problem answers)
    """
    # Split input into lines
    lines = data.strip().split("\n")

    # The last line contains operators, others contain numbers
    operator_row = lines[-1]
    number_rows = lines[:-1]

    # Process each operator
    grand_total = 0

    for i, operator in enumerate(operator_row.split()):
        if operator not in ["+", "*"]:
            raise ValueError(f"Invalid operator '{operator}' at position {i}")

        # Collect the i-th number from each row (parse on-the-fly)
        numbers = []
        for row in number_rows:
            row_nums = row.split()
            if i < len(row_nums):
                numbers.append(int(row_nums[i]))

        if not numbers:
            continue

        # Execute the operation
        if operator == "+":
            result = sum(numbers)
        else:  # '*'
            result = 1
            for num in numbers:
                result *= num

        # Add to grand total
        grand_total += result

    return grand_total


def solve_from_file(filename):
    """Read input from file and solve."""
    with open(filename, "r") as f:
        data = f.read()
    return solve(data)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
