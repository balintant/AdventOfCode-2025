#!/usr/bin/env python3
"""Test suite for Day 10: Factory"""

from part_1 import solve as solve_part1
from part_2 import solve as solve_part2


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


def test_example_part2():
    """Test Part 2 with the example from the puzzle description."""
    test_data = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]

    result = solve_part2(test_data)
    expected = 33  # 10 + 12 + 11

    print("\n" + "=" * 50)
    print("Part 2 Tests")
    print("=" * 50)
    print("\nTest: Example machines (joltage)")
    print("  Input: 3 machines")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_first_machine_part2():
    """Test the first machine individually for Part 2."""
    test_data = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    ]

    result = solve_part2(test_data)
    expected = 10

    print("\nTest: First machine joltage")
    print("  Joltages: {3,5,4,7}")
    print(f"  Expected: {expected} button presses")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_second_machine_part2():
    """Test the second machine individually for Part 2."""
    test_data = [
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    ]

    result = solve_part2(test_data)
    expected = 12

    print("\nTest: Second machine joltage")
    print("  Joltages: {7,5,12,7,2}")
    print(f"  Expected: {expected} button presses")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_third_machine_part2():
    """Test the third machine individually for Part 2."""
    test_data = [
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]

    result = solve_part2(test_data)
    expected = 11

    print("\nTest: Third machine joltage")
    print("  Joltages: {10,11,11,5,10,5}")
    print(f"  Expected: {expected} button presses")
    print(f"  Got: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("  PASS")


def test_integer_validation_part2():
    """Test that integer validation is working correctly.

    This test uses an underdetermined system where proper integer validation
    is critical. Without it, the algorithm might accept fractional solutions
    that round incorrectly.

    System: 3 counters, 4 buttons (1 free variable)
    - Button 0 affects counters [0, 1]
    - Button 1 affects counters [1, 2]
    - Button 2 affects counters [0, 2]
    - Button 3 affects counter [0]
    Target: {10, 15, 20}

    Optimal integer solution: [2, 13, 7, 1] = 23 presses
    - Button 0: 2 times → [2, 2, 0]
    - Button 1: 13 times → [2, 15, 13]
    - Button 2: 7 times → [9, 15, 20]
    - Button 3: 1 time → [10, 15, 20] ✓
    """
    test_data = [
        "[...] (0,1) (1,2) (0,2) (0) {10,15,20}",
    ]

    result = solve_part2(test_data)
    expected = 23

    print("\nTest: Integer validation (underdetermined system)")
    print("  Joltages: {10,15,20}")
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

    # Part 2 tests
    test_example_part2()
    test_first_machine_part2()
    test_second_machine_part2()
    test_third_machine_part2()
    test_integer_validation_part2()

    print("\n" + "=" * 50)
    print("All tests passed!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
