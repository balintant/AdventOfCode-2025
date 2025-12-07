#!/usr/bin/env python3
"""Test suite for Day 7: Laboratories"""

from part_1 import solve as solve_part1


def test_example_part1():
    """Test with the provided example from the puzzle."""
    data = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
    result = solve_part1(data)
    assert result == 21, f"Expected 21, got {result}"
    print("✓ Example Part 1: 21 splits")


def test_single_split_part1():
    """Test with a single splitter."""
    data = [
        "...S...",
        ".......",
        "...^...",
        ".......",
    ]
    result = solve_part1(data)
    # One beam hits one splitter = 1 split
    assert result == 1, f"Expected 1, got {result}"
    print("✓ Single split: 1 split")


def test_two_parallel_beams_part1():
    """Test with two beams that don't interact."""
    data = [
        "...S...",
        ".......",
        "...^...",
        ".......",
        "..^.^..",
        ".......",
    ]
    result = solve_part1(data)
    # First split creates 2 beams (count=1)
    # Each of those hits a splitter (count=1+2=3)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Two parallel beams: 3 splits")


def test_converging_beams_part1():
    """Test when two beams converge on the same splitter."""
    data = [
        "...S...",
        ".......",
        "...^...",
        ".......",
        "..^.^..",
        ".......",
        "...^...",
        ".......",
    ]
    result = solve_part1(data)
    # Row 2: 1 beam hits 1 splitter (count=1), creates beams at cols 2,4
    # Row 4: 2 beams hit 2 splitters (count=3), creates beams at cols 1,3,3,5 -> {1,3,5}
    # Row 6: beam at col 3 hits splitter (count=4)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Converging beams: 4 splits")


def test_no_splitters_part1():
    """Test with no splitters."""
    data = [
        "...S...",
        ".......",
        ".......",
        ".......",
    ]
    result = solve_part1(data)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ No splitters: 0 splits")


def run_tests():
    """Run all test functions."""
    print("Running Part 1 tests...")
    test_example_part1()
    test_single_split_part1()
    test_two_parallel_beams_part1()
    test_converging_beams_part1()
    test_no_splitters_part1()
    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()
