#!/usr/bin/env python3
"""
Day 11: Reactor - Part 2
https://adventofcode.com/2025/day/11

Find all paths from 'svr' to 'out' that visit both 'dac' and 'fft'.
"""

import sys


def solve(data):
    """
    Count all paths from 'svr' to 'out' that visit both 'dac' and 'fft'.

    Optimized approach using dynamic programming on a DAG.
    State: dp[node][mask] = number of paths from node to 'out' having visited
    the required nodes indicated by mask.

    Args:
        data: List of strings, each representing a device and its outputs

    Returns:
        Number of paths from 'svr' to 'out' that visit both required devices
    """
    # Parse the graph into an adjacency list
    graph = {}
    for line in data:
        if not line.strip():
            continue
        device, outputs = line.split(": ")
        graph[device] = outputs.split()

    # Memoization: key = (current_node, required_mask), value = number of paths
    # Bitmask: bit 0 = visited dac, bit 1 = visited fft
    # This works if the graph is a DAG (no cycles), which is typical for these puzzles
    memo = {}

    def count_paths(current, required_mask):
        """
        Count paths from current to 'out' that end with required_mask containing both nodes.

        This assumes the graph is acyclic (DAG), which allows clean memoization.

        Args:
            current: Current device
            required_mask: Bitmask of required devices visited so far

        Returns:
            Number of paths from current to 'out' where we visit both dac and fft
        """
        # Update required_mask if current is a required node
        if current == "dac":
            required_mask |= 1  # Set bit 0
        elif current == "fft":
            required_mask |= 2  # Set bit 1

        # Base case: reached target
        if current == "out":
            # Only count if we've visited both required devices (mask = 3 = 0b11)
            return 1 if required_mask == 3 else 0

        # Check memoization
        memo_key = (current, required_mask)
        if memo_key in memo:
            return memo[memo_key]

        # Get neighbors
        if current not in graph:
            memo[memo_key] = 0
            return 0

        # Recursively count paths through all neighbors
        total_paths = 0
        for neighbor in graph[current]:
            total_paths += count_paths(neighbor, required_mask)

        # Memoize and return
        memo[memo_key] = total_paths
        return total_paths

    return count_paths("svr", 0)


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
