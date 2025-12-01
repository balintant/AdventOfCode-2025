#!/usr/bin/env python3
"""
Tests for Day 1: Secret Entrance
"""

from solution import solve


def test_example():
    """Test with the example from the puzzle."""
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    result = solve(rotations)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Example test passed: password = 3")


def test_single_rotation_to_zero():
    """Test single rotation that lands on 0."""
    rotations = ["R50"]  # From 50, R50 -> 0
    result = solve(rotations)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Single rotation to zero test passed")


def test_wrap_around_left():
    """Test wrapping around from 0 going left."""
    rotations = ["L50", "L1"]  # 50 -> 0 -> 99
    result = solve(rotations)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Wrap around left test passed")


def test_wrap_around_right():
    """Test wrapping around from 99 going right."""
    rotations = ["R49", "R1"]  # 50 -> 99 -> 0
    result = solve(rotations)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Wrap around right test passed")


def test_no_zeros():
    """Test case where dial never lands on 0."""
    rotations = ["R10", "L5", "R3"]  # 50 -> 60 -> 55 -> 58
    result = solve(rotations)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ No zeros test passed")


def test_multiple_zeros():
    """Test multiple passes through 0."""
    rotations = ["L50", "R100", "L100"]  # 50 -> 0 -> 0 -> 0
    result = solve(rotations)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Multiple zeros test passed")


def run_tests():
    """Run all tests."""
    print("Running Day 1 tests...\n")
    test_example()
    test_single_rotation_to_zero()
    test_wrap_around_left()
    test_wrap_around_right()
    test_no_zeros()
    test_multiple_zeros()
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
