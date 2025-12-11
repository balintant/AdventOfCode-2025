# Day 11: Reactor

## Problem Summary

The factory's reactor needs to communicate with a new server rack through a network of devices. Each device can output to multiple other devices, forming a directed graph. We need to find all distinct paths through this device network.

**Part 1**: Count all distinct paths from device `you` to device `out`.

## Solution Approach

### Part 1: Path Counting with DFS ([part_1.py](part_1.py))

This is a classic **graph path enumeration problem** solved with depth-first search (DFS):

1. **Parse the graph**: Build an adjacency list from the input, where each device maps to its list of output devices
2. **DFS with backtracking**:
   - Recursively explore all paths from `you` to `out`
   - Track visited nodes to prevent cycles within a single path
   - Use backtracking to allow nodes to be reused in different paths
3. **Count paths**: Return 1 when reaching `out`, sum all paths from each neighbor

**Key Insight**: The graph is a DAG (Directed Acyclic Graph) with multiple paths converging and diverging. We need to count *all* distinct paths, not just find one path.

**Algorithm Complexity**:
- Time: O(V + E) for traversal, but with path enumeration this can be exponential in the worst case
- Space: O(V) for the recursion stack and visited set

## Test Cases

### Part 1 Tests

1. **Example test**: The puzzle's provided example with 9 devices
   - Expected: 5 distinct paths
   - Tests the basic path enumeration logic

2. **Simple linear path**: A straight line of devices
   - Expected: 1 path
   - Tests the base case

3. **Multiple routes**: Paths that diverge and converge
   - Expected: 2 paths
   - Tests that different paths through the same node are counted separately

## Results

- **Part 1**: 571 distinct paths from `you` to `out`

## Running the Solution

Using mise:
```bash
mise run solve 11 1    # Run Part 1
mise run test 11       # Run all tests
```

Direct Python:
```bash
cd days/11
python3 part_1.py      # Run Part 1
python3 test.py        # Run tests
```
