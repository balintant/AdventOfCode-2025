#!/usr/bin/env python3
"""
Day 6: Trash Compactor - Part 2
https://adventofcode.com/2025/day/6

Parse vertically-oriented cephalopod math (right-to-left columns).
Each number's digits are stacked vertically (most significant at top).
"""

import sys


def solve(data):
    """
    Solve the trash compactor math worksheet problem (cephalopod format).

    In cephalopod format, read character columns right-to-left.
    Each character column (reading top-to-bottom) forms one number.

    Args:
        data: String representing the worksheet

    Returns:
        The grand total (sum of all problem answers)
    """
    # Split input into lines, preserving trailing spaces
    lines = data.split("\n")

    # Remove only the final empty line if present
    if lines and lines[-1] == "":
        lines = lines[:-1]

    # The last line contains operators, others contain numbers
    operator_row = lines[-1]
    number_rows = lines[:-1]

    # Find the maximum line length to know how wide the worksheet is
    max_len = max(len(line) for line in lines)

    # Pad all rows to the same length to align character positions
    padded_rows = [row.ljust(max_len) for row in number_rows]
    padded_operator_row = operator_row.ljust(max_len)

    # Process operators left-to-right
    grand_total = 0
    cursor = 0

    while cursor < max_len:
        # Get the character at cursor position
        char = padded_operator_row[cursor]

        # Check if we found an operator
        if char in ["+", "*"]:
            # Find the end of this number block (next operator or EOL)
            end = cursor + 1
            while end < max_len and padded_operator_row[end] not in ["+", "*"]:
                end += 1

            # Process columns right-to-left and calculate result on-the-go
            result = 0 if char == "+" else 1
            has_numbers = False

            for col in range(end - 1, cursor - 1, -1):  # Right-to-left
                # Read this character column top-to-bottom to form one number
                digit_str = "".join(
                    padded_rows[r][col] for r in range(len(padded_rows))
                )
                digit_str = digit_str.replace(" ", "")  # Remove spaces

                if digit_str:
                    has_numbers = True
                    num = int(digit_str)
                    if char == "+":
                        result += num
                    else:  # '*'
                        result *= num

            # Add to grand total if we found any numbers
            if has_numbers:
                grand_total += result

            # Move cursor to the next operator position
            cursor = end
        else:
            cursor += 1

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
