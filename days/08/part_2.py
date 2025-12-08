#!/usr/bin/env python3
"""
Day 8: Playground - Part 2
https://adventofcode.com/2025/day/8

Continue connecting junction boxes until they're all in a single circuit.
Return the product of the X coordinates of the last pair connected.
"""

import sys
from math import sqrt


class UnionFind:
    """Disjoint set data structure for tracking connected components."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n  # Track number of separate components

    def find(self, x):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank, returns True if elements were in different sets."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        # Decrease component count since we merged two components
        self.num_components -= 1
        return True

    def is_single_component(self):
        """Check if all elements are in a single component."""
        return self.num_components == 1


def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def solve(data):
    """
    Solve the junction box connection problem for Part 2.

    Args:
        data: List of strings, each containing "X,Y,Z" coordinates

    Returns:
        Product of X coordinates of the last pair that connected all boxes
    """
    # Parse coordinates
    boxes = []
    for line in data:
        line = line.strip()
        if line:
            x, y, z = map(int, line.split(","))
            boxes.append((x, y, z))

    n = len(boxes)

    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(boxes[i], boxes[j])
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Initialize Union-Find
    uf = UnionFind(n)

    # Connect pairs until all boxes are in one circuit
    last_i, last_j = None, None
    for dist, i, j in distances:
        # Try to connect
        if uf.union(i, j):
            # This was a successful merge
            last_i, last_j = i, j
            # Check if we're done
            if uf.is_single_component():
                break

    # Return product of X coordinates of the last pair
    return boxes[last_i][0] * boxes[last_j][0]


def solve_from_file(filename):
    """Solve puzzle from input file."""
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()
    return solve(data)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
