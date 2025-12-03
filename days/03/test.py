#!/usr/bin/env python3
"""
Tests for Day 3: Lobby
"""

from part_1 import solve as solve_part1, find_max_joltage


def test_find_max_joltage():
    """Test the find_max_joltage function with individual banks."""
    assert find_max_joltage("987654321111111") == 98, "987... should produce 98"
    assert find_max_joltage("811111111111119") == 89, "811...9 should produce 89"
    assert find_max_joltage("234234234234278") == 78, "...278 should produce 78"
    assert find_max_joltage("818181911112111") == 92, "...91... should produce 92"
    assert find_max_joltage("12") == 12, "12 should produce 12"
    assert find_max_joltage("99") == 99, "99 should produce 99"
    assert find_max_joltage("123") == 23, "123 should produce 23 (max of 12, 23)"
    print("✓ find_max_joltage tests passed")


def test_example_part1():
    """Test Part 1 with the example from the puzzle."""
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    # Expected: 98 + 89 + 78 + 92 = 357
    result = solve_part1(banks)
    expected = 357
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 example test passed: total = {result}")


def test_single_bank_part1():
    """Test with a single bank."""
    banks = ["987654321"]
    # Maximum is 98 from first two digits
    result = solve_part1(banks)
    expected = 98
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 single bank test passed: total = {result}")


def test_all_same_digits_part1():
    """Test with banks of all same digits."""
    banks = ["11111", "99999"]
    # 11111 -> 11, 99999 -> 99
    result = solve_part1(banks)
    expected = 11 + 99
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 all same digits test passed: total = {result}")


def test_ascending_descending_part1():
    """Test with ascending and descending sequences."""
    banks = ["123456789", "987654321"]
    # 123456789 -> 89 (last two)
    # 987654321 -> 98 (first two)
    result = solve_part1(banks)
    expected = 89 + 98
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 ascending/descending test passed: total = {result}")


def run_tests():
    """Run all tests."""
    print("Running Day 3 tests...\n")
    print("=== Part 1 Tests ===")
    test_find_max_joltage()
    test_example_part1()
    test_single_bank_part1()
    test_all_same_digits_part1()
    test_ascending_descending_part1()
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
