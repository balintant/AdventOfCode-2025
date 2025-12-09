# Day 9: Movie Theater

## Problem Summary

The movie theater has a tile floor with red tiles at specific coordinates. The task is to find the largest rectangle that can be formed using any two red tiles as opposite corners.

### Part 1
Given a list of (x,y) coordinates of red tiles, find the maximum area of any rectangle where two red tiles serve as opposite corners.

### Part 2
(Not yet revealed)

## Solution Approach

### Part 1: [part_1.py](part_1.py)

**Algorithm:**
1. Parse the input coordinates into a list of (x,y) tuples
2. Try all possible pairs of red tiles as opposite corners
3. For each pair, calculate the rectangle area using: `(|x2-x1| + 1) × (|y2-y1| + 1)`
   - The +1 accounts for inclusive boundaries (e.g., from x=2 to x=11 spans 10 units)
4. Track and return the maximum area found

**Complexity:**
- Time: O(n²) where n is the number of red tiles
- Space: O(n) for storing coordinates

**Key Insight:**
The rectangle dimensions are calculated inclusively. A rectangle from coordinate (2,5) to (11,1) has:
- Width: |11-2| + 1 = 10 units
- Height: |5-1| + 1 = 5 units
- Area: 10 × 5 = 50 square units

This works because we're counting tiles, not distances. The tiles at positions 2 through 11 inclusive span 10 tiles.

## Test Cases

### Part 1

1. **Example from puzzle** - Verified the 50 square unit maximum area
2. **Horizontal tiles** - Two tiles on same y-coordinate: (0,0) and (5,0) → area 6
3. **Vertical tiles** - Two tiles on same x-coordinate: (0,0) and (0,3) → area 4
4. **Perfect square** - Diagonal corners (0,0) and (5,5) → area 36

All test cases pass with the implemented solution.

## Results

- **Part 1:** `4769758290`
- **Part 2:** (Not yet available)

## Running Instructions

Using mise tasks:
```bash
mise run solve 9 1    # Run Part 1
mise run test 9       # Run all tests
```

Direct Python execution:
```bash
cd days/09
python3 part_1.py              # Run Part 1 with input.txt
python3 test.py                # Run test suite
```
