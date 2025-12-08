# Day 8: Playground

## Problem Summary

The challenge involves connecting junction boxes suspended in 3D space using string lights. The goal is to determine which junction boxes to connect so that electricity can flow between them, forming circuits.

**Part 1:** After processing the 1000 closest pairs of junction boxes (by Euclidean distance), multiply together the sizes of the three largest circuits.

**Part 2:** Continue connecting the closest pairs until all junction boxes form a single circuit. Return the product of the X coordinates of the last pair that completed the circuit.

## Solution Approach

### Part 1: [part_1.py](part_1.py)

This problem is essentially a graph clustering problem where we need to:

1. **Parse 3D coordinates** from the input (X,Y,Z format)
2. **Calculate pairwise distances** between all junction boxes using Euclidean distance: `sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)`
3. **Sort pairs by distance** to identify the closest pairs
4. **Process the shortest pairs** using a Union-Find (Disjoint Set) data structure to track which boxes belong to the same circuit
5. **Count circuit sizes** and find the three largest

**Key Data Structure:** Union-Find with path compression and union by rank for efficient merging of circuits.

**Algorithm:**
- Start with each junction box as its own circuit
- Process the 1000 shortest pairs in order
- For each pair, merge their circuits (if not already merged)
- After processing all pairs, extract circuit sizes
- Return the product of the three largest circuits

**Important Detail:** The problem asks us to process the 1000 shortest *pairs* (by distance), not to make 1000 successful connections. Some pairs may already be in the same circuit, in which case the union operation doesn't change anything, but we still count it as one of the 1000 pairs processed.

### Part 2: [part_2.py](part_2.py)

Part 2 extends the same algorithm but with different stopping conditions and output:

**Algorithm:**
- Use the same Union-Find structure with component counting
- Process pairs in distance order (shortest first)
- Track the last pair that successfully merged two components
- Stop when all boxes are in a single circuit (`num_components == 1`)
- Return the product of the X coordinates of the last merged pair

**Key Difference:** Instead of stopping at a fixed number of pairs, we continue until there's only one circuit remaining. We also track which specific pair completed the merge to extract their X coordinates.

## Key Insights

1. **Union-Find is ideal** for tracking connected components efficiently
2. **Euclidean distance in 3D** is straightforward: sqrt of sum of squared differences
3. **Sorting all pairs** is O(n²log n) but necessary to process in distance order
4. **Path compression and union by rank** optimize the Union-Find operations to nearly O(1)
5. **Counting vs attempting:** We process 1000 pairs, not make 1000 successful connections

## Test Cases

### Part 1 Example:
- 20 junction boxes
- Process 10 shortest pairs
- Results in 11 circuits: [5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1]
- Product of three largest: 5 × 4 × 2 = **40** ✓

### Part 2 Example:
- Same 20 junction boxes
- Continue connecting until all form a single circuit
- Last pair connected: boxes at (216,146,977) and (117,168,530)
- Product of X coordinates: 216 × 117 = **25272** ✓

## Results

**Part 1:** `352584`

**Part 2:** `9617397716`

## Running Instructions

```bash
# Run Part 1
python3 part_1.py

# Run Part 2
python3 part_2.py

# Run with custom input
python3 part_1.py custom.txt
python3 part_2.py custom.txt

# Run all tests
python3 test.py

# Using mise tasks
mise run solve 8 1    # Part 1
mise run solve 8 2    # Part 2
mise run solve 8      # Both parts
mise run test 8       # All tests
```
