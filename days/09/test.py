#!/usr/bin/env python3
"""
Test suite for Day 9: Movie Theater
"""

from part_1 import solve as solve_part1
# from part_2 import solve as solve_part2  # Uncomment when Part 2 is ready


def test_example_part1():
    """Test with the example from the puzzle description."""
    data = [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3",
    ]

    result = solve_part1(data)
    expected = 50  # Rectangle between (2,5) and (11,1): 10×5 = 50

    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Example test passed: {result}")


def test_two_tiles_horizontal_part1():
    """Test with two tiles on the same horizontal line."""
    data = ["0,0", "5,0"]

    result = solve_part1(data)
    expected = 6  # Width: 5-0+1 = 6, Height: 0-0+1 = 1, Area: 6×1 = 6

    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Horizontal tiles test passed: {result}")


def test_two_tiles_vertical_part1():
    """Test with two tiles on the same vertical line."""
    data = ["0,0", "0,3"]

    result = solve_part1(data)
    expected = 4  # Width: 0-0+1 = 1, Height: 3-0+1 = 4, Area: 1×4 = 4

    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Vertical tiles test passed: {result}")


def test_square_part1():
    """Test with tiles forming a perfect square."""
    data = ["0,0", "5,5"]

    result = solve_part1(data)
    expected = 36  # 6×6 = 36

    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Square test passed: {result}")


def run_tests():
    """Run all test functions."""
    print("=== Part 1 Tests ===")
    test_example_part1()
    test_two_tiles_horizontal_part1()
    test_two_tiles_vertical_part1()
    test_square_part1()

    print("\n=== Part 2 Tests ===")
    print("(Part 2 not yet implemented)")

    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
