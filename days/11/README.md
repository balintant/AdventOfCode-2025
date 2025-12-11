# Day 11: Reactor

## Problem Summary

The factory's reactor needs to communicate with a new server rack through a network of devices. Each device can output to multiple other devices, forming a directed graph. We need to find all distinct paths through this device network.

**Part 1**: Count all distinct paths from device `you` to device `out`.

**Part 2**: Count all distinct paths from device `svr` (server rack) to device `out` that visit **both** `dac` (digital-to-analog converter) and `fft` (fast Fourier transform device) in any order.

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

### Part 2: Optimized DP with Bitmask State ([part_2.py](part_2.py))

Part 2 requires counting paths that visit specific required nodes. The naive DFS approach times out due to recomputing the same subproblems repeatedly.

**Optimization Strategy**: Dynamic Programming with Memoization
1. **State representation**: `(current_node, bitmask)` where bitmask tracks which required nodes we've visited
   - Bit 0 = visited `dac`
   - Bit 1 = visited `fft`
   - Only 4 possible states: `00, 01, 10, 11` (binary)
2. **Memoization**: Cache results for each `(node, bitmask)` state to avoid recomputation
3. **DAG assumption**: The graph is acyclic, so we don't need cycle detection for memoization

**Algorithm**:
```python
def count_paths(current, required_mask):
    # Update mask if current is a required node
    if current == "dac": required_mask |= 1
    if current == "fft": required_mask |= 2

    # Base case: reached target
    if current == "out":
        return 1 if required_mask == 3 else 0  # Count only if both visited

    # Check memo
    if (current, required_mask) in memo:
        return memo[(current, required_mask)]

    # Sum paths through all neighbors
    total = sum(count_paths(neighbor, required_mask) for neighbor in graph[current])

    memo[(current, required_mask)] = total
    return total
```

**Key Insight**: By assuming the graph is a DAG (which it is for AoC puzzles), we can memoize cleanly without worrying about cycles. Each unique `(node, mask)` state is computed exactly once.

**Algorithm Complexity**:
- Time: O(V × 2^k × E) where k = number of required nodes (k=2, so 4 states)
- Space: O(V × 2^k) for memoization table
- In practice: Runs in milliseconds vs timing out with naive approach

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

### Part 2 Tests

1. **Example test**: The puzzle's provided example with 13 devices
   - Expected: 2 paths (out of 8 total) that visit both `dac` and `fft`
   - Tests the constrained path counting logic

2. **Single required node**: Path that only visits `dac` but not `fft`
   - Expected: 0 paths
   - Ensures we require BOTH nodes, not just one

3. **Both required nodes**: Path that visits both `dac` and `fft`
   - Expected: 1 path
   - Tests the basic constraint satisfaction

## Results

- **Part 1**: 571 distinct paths from `you` to `out`
- **Part 2**: 511378159390560 paths from `svr` to `out` that visit both `dac` and `fft`

## Running the Solution

Using mise:
```bash
mise run solve 11      # Run both parts
mise run solve 11 1    # Run Part 1
mise run solve 11 2    # Run Part 2
mise run test 11       # Run all tests
```

Direct Python:
```bash
cd days/11
python3 part_1.py      # Run Part 1
python3 part_2.py      # Run Part 2
python3 test.py        # Run tests
```
