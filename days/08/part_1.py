#!/usr/bin/env python3
"""
Day 8: Playground - Part 1
https://adventofcode.com/2025/day/8

Connect the 1000 closest pairs of junction boxes and find the product
of the three largest circuit sizes.
"""

import sys
from math import sqrt


class UnionFind:
    """Disjoint set data structure for tracking connected components."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  # Track size of each component

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
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1

        return True

    def get_component_sizes(self):
        """Get sizes of all components."""
        root_sizes = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in root_sizes:
                root_sizes[root] = self.size[root]
        return list(root_sizes.values())


def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def solve(data, num_connections=1000):
    """
    Solve the junction box connection problem.

    Args:
        data: List of strings, each containing "X,Y,Z" coordinates
        num_connections: Number of shortest connections to make (default 1000)

    Returns:
        Product of the three largest circuit sizes after making the connections
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

    # Make connections (process num_connections shortest pairs)
    for idx, (dist, i, j) in enumerate(distances):
        if idx >= num_connections:
            break
        # Try to connect (may already be in same circuit)
        uf.union(i, j)

    # Get component sizes
    sizes = uf.get_component_sizes()
    sizes.sort(reverse=True)

    # Return product of three largest
    return sizes[0] * sizes[1] * sizes[2]


def solve_from_file(filename, num_connections=1000):
    """Solve puzzle from input file."""
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()
    return solve(data, num_connections)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
