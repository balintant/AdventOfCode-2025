#!/usr/bin/env python3
"""Test suite for Day 12: Christmas Tree Farm"""

from part_1 import solve as solve_part1


def test_example_part1():
    """Test with the example from the puzzle description."""
    example = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
    result = solve_part1(example)
    assert result == 2, f"Expected 2, got {result}"
    print("✓ Part 1 example test passed")


def test_single_shape_fits():
    """Test a simple case where a single shape fits."""
    data = """0:
##
##

3x3: 1
"""
    result = solve_part1(data)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Single shape fits test passed")


def test_single_shape_doesnt_fit():
    """Test a case where a shape is too big for the region."""
    data = """0:
###
###

2x2: 1
"""
    result = solve_part1(data)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Single shape doesn't fit test passed")


def test_rotation_needed():
    """Test a case where rotation is needed to fit."""
    data = """0:
###
#..

2x3: 1
"""
    result = solve_part1(data)
    # The shape is 2x3 in one orientation, 3x2 in another
    # A 2x3 region should be able to fit it rotated
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Rotation needed test passed")


def run_tests():
    """Run all tests."""
    print("=" * 50)
    print("Part 1 Tests")
    print("=" * 50)
    test_example_part1()
    test_single_shape_fits()
    test_single_shape_doesnt_fit()
    test_rotation_needed()
    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()
