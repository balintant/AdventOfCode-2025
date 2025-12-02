#!/usr/bin/env python3
"""
Tests for Day 2: Gift Shop
"""

from part_1 import solve as solve_part1, is_invalid_id
from part_2 import solve as solve_part2, is_invalid_id as is_invalid_id_part2


def test_is_invalid_id():
    """Test the is_invalid_id function with various cases."""
    # Valid invalid IDs (repeated patterns)
    assert is_invalid_id(11), "11 should be invalid (1 repeated)"
    assert is_invalid_id(22), "22 should be invalid (2 repeated)"
    assert is_invalid_id(55), "55 should be invalid (5 repeated)"
    assert is_invalid_id(99), "99 should be invalid (9 repeated)"
    assert is_invalid_id(1010), "1010 should be invalid (10 repeated)"
    assert is_invalid_id(6464), "6464 should be invalid (64 repeated)"
    assert is_invalid_id(123123), "123123 should be invalid (123 repeated)"
    assert is_invalid_id(222222), "222222 should be invalid (222 repeated)"
    assert is_invalid_id(446446), "446446 should be invalid (446 repeated)"
    assert is_invalid_id(1188511885), "1188511885 should be invalid (11885 repeated)"
    assert is_invalid_id(38593859), "38593859 should be invalid (3859 repeated)"

    # Valid IDs (not repeated patterns)
    assert not is_invalid_id(101), "101 should be valid (odd length)"
    assert not is_invalid_id(12), "12 should be valid (not repeated)"
    assert not is_invalid_id(1234), "1234 should be valid (not repeated)"
    assert not is_invalid_id(100), "100 should be valid (odd length)"
    assert not is_invalid_id(1011), "1011 should be valid (10 != 11)"
    assert not is_invalid_id(565656), "565656 should be valid (565 != 656)"

    # Leading zero cases (should be valid IDs, not invalid)
    # Note: 0101 would be "01" repeated, but since 01 starts with 0, it's not a valid product ID at all
    # So we won't encounter it, but our function should still handle it correctly
    # The number 101 is valid and should not be flagged as invalid

    print("✓ is_invalid_id tests passed")


def test_example_part1():
    """Test Part 1 with the example from the puzzle."""
    ranges = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]

    # Expected invalid IDs from the example:
    # 11-22: 11, 22
    # 95-115: 99
    # 998-1012: 1010
    # 1188511880-1188511890: 1188511885
    # 222220-222224: 222222
    # 446443-446449: 446446
    # 38593856-38593862: 38593859
    # Others: none

    result = solve_part1(ranges)
    expected = 1227775554
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 example test passed: sum = {result}")


def test_single_range_part1():
    """Test with a single range containing invalid IDs."""
    ranges = ["10-20"]
    # Should find: 11
    result = solve_part1(ranges)
    expected = 11
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 single range test passed: sum = {result}")


def test_no_invalid_ids_part1():
    """Test with a range containing no invalid IDs."""
    ranges = ["100-110"]
    result = solve_part1(ranges)
    expected = 0
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 no invalid IDs test passed: sum = {result}")


def test_multiple_invalid_in_range_part1():
    """Test with a range containing multiple invalid IDs."""
    ranges = ["10-100"]
    # Should find: 11, 22, 33, 44, 55, 66, 77, 88, 99
    result = solve_part1(ranges)
    expected = 11 + 22 + 33 + 44 + 55 + 66 + 77 + 88 + 99
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 multiple invalid IDs test passed: sum = {result}")


def test_is_invalid_id_part2():
    """Test the Part 2 is_invalid_id function with various cases."""
    # Valid invalid IDs (repeated patterns - 2 or more times)
    assert is_invalid_id_part2(11), "11 should be invalid (1 repeated 2 times)"
    assert is_invalid_id_part2(111), "111 should be invalid (1 repeated 3 times)"
    assert is_invalid_id_part2(1111), "1111 should be invalid (1 repeated 4 times)"
    assert is_invalid_id_part2(99), "99 should be invalid (9 repeated 2 times)"
    assert is_invalid_id_part2(999), "999 should be invalid (9 repeated 3 times)"
    assert is_invalid_id_part2(1010), "1010 should be invalid (10 repeated 2 times)"
    assert is_invalid_id_part2(123123), (
        "123123 should be invalid (123 repeated 2 times)"
    )
    assert is_invalid_id_part2(123123123), (
        "123123123 should be invalid (123 repeated 3 times)"
    )
    assert is_invalid_id_part2(12341234), (
        "12341234 should be invalid (1234 repeated 2 times)"
    )
    assert is_invalid_id_part2(1212121212), (
        "1212121212 should be invalid (12 repeated 5 times)"
    )
    assert is_invalid_id_part2(565656), "565656 should be invalid (56 repeated 3 times)"
    assert is_invalid_id_part2(824824824), (
        "824824824 should be invalid (824 repeated 3 times)"
    )
    assert is_invalid_id_part2(2121212121), (
        "2121212121 should be invalid (21 repeated 5 times)"
    )

    # Valid IDs (not repeated patterns)
    assert not is_invalid_id_part2(101), "101 should be valid (odd length, no pattern)"
    assert not is_invalid_id_part2(12), "12 should be valid (not repeated)"
    assert not is_invalid_id_part2(1234), "1234 should be valid (not repeated)"
    assert not is_invalid_id_part2(1011), "1011 should be valid (10 != 11)"

    print("✓ Part 2 is_invalid_id tests passed")


def test_example_part2():
    """Test Part 2 with the example from the puzzle."""
    ranges = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]

    # Expected invalid IDs from the example:
    # 11-22: 11, 22
    # 95-115: 99, 111
    # 998-1012: 999, 1010
    # 1188511880-1188511890: 1188511885
    # 222220-222224: 222222
    # 446443-446449: 446446
    # 38593856-38593862: 38593859
    # 565653-565659: 565656
    # 824824821-824824827: 824824824
    # 2121212118-2121212124: 2121212121

    result = solve_part2(ranges)
    expected = 4174379265
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 example test passed: sum = {result}")


def test_triple_pattern_part2():
    """Test Part 2 with patterns repeated 3 times."""
    ranges = ["110-112"]
    # Should find: 111 (1 repeated 3 times)
    result = solve_part2(ranges)
    expected = 111
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 triple pattern test passed: sum = {result}")


def test_multiple_repetition_part2():
    """Test Part 2 with various repetition counts."""
    ranges = ["1-1000"]
    # Should find all patterns repeated 2+ times
    # Includes: 11, 22, ..., 99 (2x), 111, 222, ..., 999 (3x)
    result = solve_part2(ranges)
    # Just verify it runs and finds more than Part 1 would
    assert result > 0, "Should find invalid IDs"
    print(f"✓ Part 2 multiple repetition test passed: sum = {result}")


def run_tests():
    """Run all tests."""
    print("Running Day 2 tests...\n")
    print("=== Part 1 Tests ===")
    test_is_invalid_id()
    test_example_part1()
    test_single_range_part1()
    test_no_invalid_ids_part1()
    test_multiple_invalid_in_range_part1()
    print("\n=== Part 2 Tests ===")
    test_is_invalid_id_part2()
    test_example_part2()
    test_triple_pattern_part2()
    test_multiple_repetition_part2()
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
