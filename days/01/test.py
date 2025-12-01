#!/usr/bin/env python3
"""
Tests for Day 1: Secret Entrance
"""

from solution_part1 import solve as solve_part1
from solution_part2 import solve as solve_part2


def test_example_part1():
    """Test Part 1 with the example from the puzzle."""
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    result = solve_part1(rotations)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Part 1 example test passed: password = 3")


def test_example_part2():
    """Test Part 2 with the example from the puzzle."""
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    # From instructions: 3 times at end + 3 times during = 6
    # L68 from 50: passes through 0 once (50->49->...->1->0->99->...->82)
    # R48 from 52: ends at 0
    # R60 from 95: passes through 0 once (95->96->...->99->0->...->55)
    # L55 from 55: ends at 0
    # L99 from 99: ends at 0
    # L82 from 14: passes through 0 once (14->13->...->1->0->99->...->32)
    result = solve_part2(rotations)
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Part 2 example test passed: password = 6")


def test_single_rotation_to_zero_part2():
    """Test single rotation that lands on 0 (Part 2)."""
    rotations = ["R50"]  # From 50, R50 -> 0 (ends at 0)
    result = solve_part2(rotations)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Part 2: Single rotation to zero test passed")


def test_multiple_wraps_part2():
    """Test rotation that wraps multiple times (Part 2)."""
    # From instructions: R1000 from 50 passes through 0 ten times
    rotations = ["R1000"]  # 1000 clicks = 10 complete wraps
    result = solve_part2(rotations)
    assert result == 10, f"Expected 10, got {result}"
    print("✓ Part 2: Multiple wraps test passed (R1000 = 10 passes)")


def test_pass_through_during_rotation_part2():
    """Test passing through 0 during rotation (Part 2)."""
    rotations = [
        "L60"
    ]  # From 50, L60 -> 90 (passes through 0: 50->...->0->99->...->90)
    result = solve_part2(rotations)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Part 2: Pass through during rotation test passed")


def test_no_zeros_part2():
    """Test case where dial never passes through 0 (Part 2)."""
    rotations = ["R10", "L5", "R3"]  # 50 -> 60 -> 55 -> 58
    result = solve_part2(rotations)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Part 2: No zeros test passed")


def test_exact_wrap_part2():
    """Test exact 100-click wrap (Part 2)."""
    rotations = ["R100"]  # From 50, R100 -> 50 (passes through 0 once)
    result = solve_part2(rotations)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Part 2: Exact wrap test passed")


def run_tests():
    """Run all tests."""
    print("Running Day 1 tests...\n")
    print("=== Part 1 Tests ===")
    test_example_part1()
    print("\n=== Part 2 Tests ===")
    test_example_part2()
    test_single_rotation_to_zero_part2()
    test_multiple_wraps_part2()
    test_pass_through_during_rotation_part2()
    test_no_zeros_part2()
    test_exact_wrap_part2()
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
