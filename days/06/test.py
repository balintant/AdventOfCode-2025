#!/usr/bin/env python3
"""
Test suite for Day 6: Trash Compactor
"""

from part_1 import solve as solve_part1


def test_example_part1():
    """Test with the example from the puzzle instructions."""
    example_input = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

    result = solve_part1(example_input)
    expected = 4277556  # 33210 + 490 + 4243455 + 401

    # Break down the problems:
    # Problem 1: 123 * 45 * 6 = 33210
    # Problem 2: 328 + 64 + 98 = 490
    # Problem 3: 51 * 387 * 215 = 4243455
    # Problem 4: 64 + 23 + 314 = 401
    # Grand total: 33210 + 490 + 4243455 + 401 = 4277556

    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Example test passed: {result}")


def test_single_addition_part1():
    """Test a single addition problem."""
    test_input = """10
20
30
+"""
    result = solve_part1(test_input)
    expected = 60  # 10 + 20 + 30
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Single addition test passed: {result}")


def test_single_multiplication_part1():
    """Test a single multiplication problem."""
    test_input = """5
4
3
*"""
    result = solve_part1(test_input)
    expected = 60  # 5 * 4 * 3
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Single multiplication test passed: {result}")


def test_two_problems_part1():
    """Test with two problems side by side."""
    test_input = """10  5
20  3
+   *"""
    result = solve_part1(test_input)
    expected = 45  # (10 + 20) + (5 * 3) = 30 + 15 = 45
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Two problems test passed: {result}")


def run_tests():
    """Run all test functions."""
    print("Running Part 1 tests...")
    print()

    test_example_part1()
    test_single_addition_part1()
    test_single_multiplication_part1()
    test_two_problems_part1()

    print()
    print("All tests passed! ✓")


if __name__ == "__main__":
    run_tests()
