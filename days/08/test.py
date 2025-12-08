#!/usr/bin/env python3
"""Test suite for Day 8: Playground"""

from part_1 import solve as solve_part1
from part_2 import solve as solve_part2


def test_example_part1():
    """Test with the example from the puzzle description."""
    data = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]

    # After making the 10 shortest connections:
    # - One circuit with 5 boxes
    # - One circuit with 4 boxes
    # - Two circuits with 2 boxes each
    # - Seven circuits with 1 box each
    # Product of three largest: 5 * 4 * 2 = 40
    result = solve_part1(data, num_connections=10)
    expected = 40

    # Debug: check what sizes we actually got
    from part_1 import UnionFind, euclidean_distance

    boxes = []
    for line in data:
        x, y, z = map(int, line.split(","))
        boxes.append((x, y, z))

    n = len(boxes)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(boxes[i], boxes[j])
            distances.append((dist, i, j))
    distances.sort()

    uf = UnionFind(n)
    for idx, (dist, i, j) in enumerate(distances):
        if idx >= 10:
            break
        uf.union(i, j)

    sizes = uf.get_component_sizes()
    sizes.sort(reverse=True)
    print(f"Circuit sizes: {sizes}")
    print(f"Three largest: {sizes[0]}, {sizes[1]}, {sizes[2]}")
    print(f"Product: {sizes[0] * sizes[1] * sizes[2]}")

    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Example test passed: {result}")


def test_example_part2():
    """Test Part 2 with the example from the puzzle description."""
    data = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]

    # The last connection to form a single circuit is between
    # junction boxes at 216,146,977 and 117,168,530
    # Product of X coordinates: 216 * 117 = 25272
    result = solve_part2(data)
    expected = 25272
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 example test passed: {result}")


def run_tests():
    """Run all tests."""
    print("Running Part 1 tests...")
    test_example_part1()
    print("\nRunning Part 2 tests...")
    test_example_part2()
    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()
