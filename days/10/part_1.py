#!/usr/bin/env python3
"""Day 10: Factory - Part 1

https://adventofcode.com/2025/day/10

Solve the indicator light problem by finding minimum button presses using
Gaussian elimination over GF(2) (binary field).
"""

import sys
import re


def parse_machine(line):
    """Parse a machine specification line.

    Returns:
        target: list of bools representing desired light states
        buttons: list of lists of light indices that each button toggles
        joltages: list of joltage values (ignored for Part 1)
    """
    # Extract the three parts: [pattern], (buttons), {joltages}
    pattern_match = re.search(r"\[([.#]+)\]", line)
    buttons_text = re.findall(r"\(([0-9,]+)\)", line)
    joltages_text = re.search(r"\{([0-9,]+)\}", line)

    # Parse target pattern
    target = [c == "#" for c in pattern_match.group(1)]

    # Parse buttons (each button is a list of light indices it toggles)
    buttons = []
    for btn_text in buttons_text:
        indices = [int(x) for x in btn_text.split(",")]
        buttons.append(indices)

    # Parse joltages (not used in Part 1)
    joltages = [int(x) for x in joltages_text.group(1).split(",")]

    return target, buttons, joltages


def gauss_elimination_gf2(matrix, target):
    """Solve a system of linear equations over GF(2) using Gaussian elimination.

    This finds ALL solutions by identifying free variables and enumerating them.
    Returns the solution with minimum sum (minimum button presses).

    Args:
        matrix: list of lists, where matrix[light_idx][button_idx] = 1 if button affects light
        target: list of bools, desired state for each light

    Returns:
        solution: list of button press counts (all 0 or 1 in GF(2)) with minimum sum
        or None if no solution exists
    """
    n_lights = len(matrix)
    n_buttons = len(matrix[0]) if n_lights > 0 else 0

    # Create augmented matrix [A | b]
    aug = [row[:] + [int(target[i])] for i, row in enumerate(matrix)]

    # Track which column is the pivot for each row
    pivot_cols = []

    # Forward elimination (reduced row echelon form)
    current_row = 0
    for col in range(n_buttons):
        # Find pivot in this column
        pivot_row = None
        for row in range(current_row, n_lights):
            if aug[row][col] == 1:
                pivot_row = row
                break

        if pivot_row is None:
            # No pivot in this column - this is a free variable
            continue

        # Swap rows if needed
        if pivot_row != current_row:
            aug[current_row], aug[pivot_row] = aug[pivot_row], aug[current_row]

        # Record pivot
        pivot_cols.append((current_row, col))

        # Eliminate both above and below (RREF)
        for row in range(n_lights):
            if row != current_row and aug[row][col] == 1:
                for j in range(n_buttons + 1):
                    aug[row][j] ^= aug[current_row][j]

        current_row += 1

    # Check for inconsistency
    for i in range(n_lights):
        if all(aug[i][j] == 0 for j in range(n_buttons)) and aug[i][n_buttons] == 1:
            return None  # No solution

    # Identify free variables (columns without pivots)
    pivot_col_set = {col for _, col in pivot_cols}
    free_vars = [col for col in range(n_buttons) if col not in pivot_col_set]

    # If no free variables, there's a unique solution
    if not free_vars:
        solution = [0] * n_buttons
        for row, col in pivot_cols:
            solution[col] = aug[row][n_buttons]
        return solution

    # Enumerate all combinations of free variables to find minimum
    min_presses = float("inf")
    best_solution = None

    for mask in range(1 << len(free_vars)):
        # Set free variables according to mask
        solution = [0] * n_buttons
        for i, var_idx in enumerate(free_vars):
            solution[var_idx] = (mask >> i) & 1

        # Compute dependent variables
        for row, col in pivot_cols:
            val = aug[row][n_buttons]
            for j in range(col + 1, n_buttons):
                val ^= aug[row][j] * solution[j]
            solution[col] = val

        # Count presses
        presses = sum(solution)
        if presses < min_presses:
            min_presses = presses
            best_solution = solution

    return best_solution


def solve_machine(target, buttons):
    """Solve a single machine's light configuration problem.

    Returns:
        Minimum number of button presses, or None if unsolvable
    """
    n_lights = len(target)
    n_buttons = len(buttons)

    # Build matrix where matrix[i][j] = 1 if button j affects light i
    matrix = [[0] * n_buttons for _ in range(n_lights)]
    for btn_idx, light_indices in enumerate(buttons):
        for light_idx in light_indices:
            matrix[light_idx][btn_idx] = 1

    # Solve using Gaussian elimination
    solution = gauss_elimination_gf2(matrix, target)

    if solution is None:
        return None

    # Count button presses (in GF(2), all values are 0 or 1)
    return sum(solution)


def solve(data):
    """Solve the puzzle for all machines.

    Args:
        data: list of machine specification strings

    Returns:
        Total minimum button presses across all machines
    """
    total_presses = 0

    for line in data:
        if not line.strip():
            continue

        target, buttons, _ = parse_machine(line)
        presses = solve_machine(target, buttons)

        if presses is None:
            raise ValueError(f"No solution found for machine: {line}")

        total_presses += presses

    return total_presses


def solve_from_file(filename):
    """Read input from file and solve."""
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
