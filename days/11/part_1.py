#!/usr/bin/env python3
"""
Day 11: Reactor - Part 1
https://adventofcode.com/2025/day/11

Find all distinct paths from device 'you' to device 'out'.
"""

import sys


def solve(data):
    """
    Count all distinct paths from 'you' to 'out' in the device graph.

    Args:
        data: List of strings, each representing a device and its outputs

    Returns:
        Number of distinct paths from 'you' to 'out'
    """
    # Parse the graph into an adjacency list
    graph = {}
    for line in data:
        if not line.strip():
            continue
        device, outputs = line.split(": ")
        graph[device] = outputs.split()

    # DFS to find all paths from 'you' to 'out'
    def count_paths(current, target, visited):
        """
        Count all paths from current to target.

        Args:
            current: Current device
            target: Target device ('out')
            visited: Set of visited devices on current path (to avoid cycles)

        Returns:
            Number of paths from current to target
        """
        if current == target:
            return 1

        if current not in graph:
            return 0

        # Mark current as visited to avoid cycles
        visited.add(current)

        total_paths = 0
        for neighbor in graph[current]:
            if neighbor not in visited:
                total_paths += count_paths(neighbor, target, visited)

        # Backtrack: unmark current so other paths can use it
        visited.remove(current)

        return total_paths

    return count_paths("you", "out", set())


def solve_from_file(filename):
    """Read input from file and solve the puzzle."""
    with open(filename, "r") as f:
        data = [line.rstrip("\n") for line in f]
    return solve(data)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
