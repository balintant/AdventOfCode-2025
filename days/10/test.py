#!/usr/bin/env python3
"""Test suite for Day 10: Factory"""

from part_1 import solve as solve_part1


def test_example_part1():
    """Test with the example from the puzzle description."""
    test_data = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]

    result = solve_part1(test_data)
    expected = 7  # 2 + 3 + 2

    print("Test: Example machines")
    print("  Input: 3 machines")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_first_machine_part1():
    """Test the first machine individually."""
    test_data = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    ]

    result = solve_part1(test_data)
    expected = 2

    print("\nTest: First machine only")
    print("  Pattern: [.##.]")
    print(f"  Expected: {expected} button presses")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_second_machine_part1():
    """Test the second machine individually."""
    test_data = [
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    ]

    result = solve_part1(test_data)
    expected = 3

    print("\nTest: Second machine only")
    print("  Pattern: [...#.]")
    print(f"  Expected: {expected} button presses")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_third_machine_part1():
    """Test the third machine individually."""
    test_data = [
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]

    result = solve_part1(test_data)
    expected = 2

    print("\nTest: Third machine only")
    print("  Pattern: [.###.#]")
    print(f"  Expected: {expected} button presses")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def run_tests():
    """Run all tests."""
    print("=" * 50)
    print("Running Day 10 Tests - Part 1")
    print("=" * 50)

    test_example_part1()
    test_first_machine_part1()
    test_second_machine_part1()
    test_third_machine_part1()

    print("\n" + "=" * 50)
    print("All tests passed!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
