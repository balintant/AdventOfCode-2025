#!/usr/bin/env python3
"""
Test suite for Day 11: Reactor
"""

from part_1 import solve as solve_part1
from part_2 import solve as solve_part2


def test_example_part1():
    """Test with the example from the puzzle description."""
    data = [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out",
    ]
    # Expected paths:
    # 1. you -> bbb -> ddd -> ggg -> out
    # 2. you -> bbb -> eee -> out
    # 3. you -> ccc -> ddd -> ggg -> out
    # 4. you -> ccc -> eee -> out
    # 5. you -> ccc -> fff -> out
    result = solve_part1(data)
    assert result == 5, f"Expected 5 paths, got {result}"
    print("✓ Part 1 - Example test passed")


def test_simple_path_part1():
    """Test with a simple linear path."""
    data = [
        "you: a",
        "a: b",
        "b: out",
    ]
    # Only one path: you -> a -> b -> out
    result = solve_part1(data)
    assert result == 1, f"Expected 1 path, got {result}"
    print("✓ Part 1 - Simple linear path test passed")


def test_multiple_routes_part1():
    """Test with multiple diverging and converging paths."""
    data = [
        "you: a b",
        "a: c",
        "b: c",
        "c: out",
    ]
    # Two paths:
    # 1. you -> a -> c -> out
    # 2. you -> b -> c -> out
    result = solve_part1(data)
    assert result == 2, f"Expected 2 paths, got {result}"
    print("✓ Part 1 - Multiple routes test passed")


def test_example_part2():
    """Test Part 2 with the example from the puzzle description."""
    data = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]
    # Total 8 paths from svr to out
    # Only 2 paths visit both dac and fft:
    # 1. svr -> aaa -> fft -> ccc -> eee -> dac -> fff -> ggg -> out
    # 2. svr -> aaa -> fft -> ccc -> eee -> dac -> fff -> hhh -> out
    result = solve_part2(data)
    assert result == 2, f"Expected 2 paths visiting both dac and fft, got {result}"
    print("✓ Part 2 - Example test passed")


def test_single_required_node_part2():
    """Test that paths must visit BOTH required nodes."""
    data = [
        "svr: dac",
        "dac: out",
    ]
    # This path only visits dac, not fft - should return 0
    result = solve_part2(data)
    assert result == 0, f"Expected 0 paths (missing fft), got {result}"
    print("✓ Part 2 - Single required node test passed")


def test_both_required_nodes_part2():
    """Test that paths visiting both required nodes are counted."""
    data = [
        "svr: dac",
        "dac: fft",
        "fft: out",
    ]
    # This path visits both dac and fft - should return 1
    result = solve_part2(data)
    assert result == 1, f"Expected 1 path (visits both dac and fft), got {result}"
    print("✓ Part 2 - Both required nodes test passed")


def run_tests():
    """Run all test functions."""
    print("\n=== Part 1 Tests ===")
    test_example_part1()
    test_simple_path_part1()
    test_multiple_routes_part1()

    print("\n=== Part 2 Tests ===")
    test_example_part2()
    test_single_required_node_part2()
    test_both_required_nodes_part2()

    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
