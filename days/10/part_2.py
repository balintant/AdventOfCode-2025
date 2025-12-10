#!/usr/bin/env python3
"""Day 10: Factory - Part 2

https://adventofcode.com/2025/day/10

Solve the joltage counter problem by finding minimum button presses to reach
target counter values. This is a system of linear Diophantine equations.
"""

import sys
import re


def parse_machine(line):
    """Parse a machine specification line.

    Returns:
        buttons: list of lists of counter indices that each button affects
        joltages: list of target joltage values
    """
    # Extract the button wiring and joltage requirements
    buttons_text = re.findall(r"\(([0-9,]+)\)", line)
    joltages_text = re.search(r"\{([0-9,]+)\}", line)

    # Parse buttons (each button is a list of counter indices it affects)
    buttons = []
    for btn_text in buttons_text:
        indices = [int(x) for x in btn_text.split(",")]
        buttons.append(indices)

    # Parse joltages (target counter values)
    joltages = [int(x) for x in joltages_text.group(1).split(",")]

    return buttons, joltages


def solve_integer_system(matrix, target):
    """Solve a system of linear equations over integers using Gaussian elimination.

    We want to find x such that Ax = b with x ≥ 0 and minimize sum(x).

    Uses RREF to identify free variables, then enumerates them with a proper bound:
    max(target) is an upper limit since no single button press can need more than
    the maximum target value.

    Args:
        matrix: list of lists, where matrix[counter_idx][button_idx] = 1 if button affects counter
        target: list of ints, target value for each counter

    Returns:
        solution: list of button press counts (non-negative integers)
        or None if no solution exists
    """
    n_counters = len(matrix)
    n_buttons = len(matrix[0]) if n_counters > 0 else 0

    # Create augmented matrix [A | b] (work with floats for Gaussian elimination)
    aug = [row[:] + [float(target[i])] for i, row in enumerate(matrix)]

    # Track which column is the pivot for each row
    pivot_cols = []

    # Forward elimination (reduced row echelon form)
    current_row = 0
    for col in range(n_buttons):
        # Find pivot in this column
        pivot_row = None
        for row in range(current_row, n_counters):
            if abs(aug[row][col]) > 1e-9:
                pivot_row = row
                break

        if pivot_row is None:
            # No pivot in this column - this is a free variable
            continue

        # Swap rows if needed
        if pivot_row != current_row:
            aug[current_row], aug[pivot_row] = aug[pivot_row], aug[current_row]

        # Scale pivot row to make pivot = 1
        pivot_val = aug[current_row][col]
        for j in range(n_buttons + 1):
            aug[current_row][j] /= pivot_val

        # Record pivot
        pivot_cols.append((current_row, col))

        # Eliminate both above and below (RREF)
        for row in range(n_counters):
            if row != current_row and abs(aug[row][col]) > 1e-9:
                factor = aug[row][col]
                for j in range(n_buttons + 1):
                    aug[row][j] -= factor * aug[current_row][j]

        current_row += 1

    # Check for inconsistency
    for i in range(n_counters):
        if (
            all(abs(aug[i][j]) < 1e-9 for j in range(n_buttons))
            and abs(aug[i][n_buttons]) > 1e-9
        ):
            return None  # No solution

    # Build the solution by setting free variables and computing pivot variables
    pivot_col_set = {col for _, col in pivot_cols}
    free_vars = [col for col in range(n_buttons) if col not in pivot_col_set]

    # If no free variables, unique solution
    if not free_vars:
        solution = [0.0] * n_buttons
        for row, col in pivot_cols:
            val = aug[row][n_buttons]
            if val < -1e-9:
                return None
            solution[col] = val
        return [round(x) for x in solution]

    # With free variables: use branch-and-bound with max(target) as upper bound
    # For any single button press to contribute to a counter, it can't exceed the
    # maximum target value. With proper integer validation (not just rounding at the end),
    # this bound is sufficient to find optimal integer solutions.
    best_solution = None
    min_presses = float("inf")

    # Upper bound: max(target) - no single free variable should need more than this
    max_free_val = max(target)

    # Branch and bound with pruning
    def search(index, current_solution, current_sum):
        nonlocal best_solution, min_presses

        # Pruning: if current sum already too high, abort
        if current_sum >= min_presses:
            return

        if index == len(free_vars):
            # All free variables set, compute pivot variables
            solution = current_solution[:]
            total_sum = current_sum
            valid = True

            for row, col in pivot_cols:
                val = aug[row][n_buttons]
                for j in range(n_buttons):
                    if j != col:
                        val -= aug[row][j] * solution[j]

                # Check if value is close enough to an integer
                rounded_val = round(val)
                if abs(val - rounded_val) > 1e-6:
                    valid = False  # Not an integer solution
                    break

                if rounded_val < 0:
                    valid = False
                    break

                solution[col] = float(rounded_val)
                total_sum += rounded_val

                # Early abort if already too high
                if total_sum >= min_presses:
                    valid = False
                    break

            if valid and total_sum < min_presses:
                min_presses = total_sum
                best_solution = [int(x) for x in solution]
            return

        # Try values in ascending order (smaller values more likely optimal)
        free_var_idx = free_vars[index]
        upper_limit = max_free_val + 1
        if min_presses < float("inf"):
            upper_limit = min(upper_limit, int(min_presses - current_sum))
        for val in range(upper_limit):
            current_solution[free_var_idx] = float(val)
            search(index + 1, current_solution, current_sum + val)

    initial_solution = [0.0] * n_buttons
    search(0, initial_solution, 0.0)

    return best_solution


def solve_machine(buttons, joltages):
    """Solve a single machine's joltage configuration problem.

    Args:
        buttons: list of lists of counter indices that each button affects
        joltages: list of target joltage values

    Returns:
        Minimum number of button presses, or None if unsolvable
    """
    n_counters = len(joltages)
    n_buttons = len(buttons)

    # Build matrix where matrix[i][j] = 1 if button j affects counter i
    matrix = [[0] * n_buttons for _ in range(n_counters)]
    for btn_idx, counter_indices in enumerate(buttons):
        for counter_idx in counter_indices:
            if counter_idx < n_counters:  # Safety check
                matrix[counter_idx][btn_idx] = 1

    # Solve using Gaussian elimination
    solution = solve_integer_system(matrix, joltages)

    if solution is None:
        return None

    # Count button presses
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

        buttons, joltages = parse_machine(line)
        presses = solve_machine(buttons, joltages)

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
