# Day 12: Christmas Tree Farm

**Problem**: [Advent of Code 2025 Day 12](https://adventofcode.com/2025/day/12)

## Problem Summary

**Part 1**: Determine how many regions under Christmas trees can fit all their required presents. Presents come in 6 standard polyomino shapes that can be rotated and flipped. Each region specifies its dimensions and the quantity of each shape type that must fit inside. Shapes cannot overlap (their `#` cells can't occupy the same grid position), but they can fit together (the `.` cells in a shape's definition don't block other shapes).

**Part 2**: Narrative conclusion - the Elves are grateful, a star magically appears on a Christmas tree. No additional puzzle to solve.

## Solution Approach

### Part 1: Hybrid Greedy/DLX Packing - [part_1.py](part_1.py)

The solution uses a **hybrid approach** that combines greedy placement with Dancing Links (DLX):

1. **Quick Area Check**: First eliminate regions where total shape area exceeds grid area (586/1000 regions fail this check immediately)

2. **Gap-Based Algorithm Selection**:
   - **Large gaps (>100 cells)**: Use greedy placement
     - Try each shape in order, placing it at the first available position
     - Much faster (O(shapes × orientations × grid_size))
     - Sufficient when there's plenty of space
   - **Small gaps (≤100 cells)**: Use DLX exact cover
     - Model as exact cover with primary columns (shape instances) and secondary columns (grid cells)
     - Uses Knuth's Algorithm X with Dancing Links for efficient backtracking
     - Necessary for tight-fitting puzzles

3. **Shape Representation**:
   - Parse shapes into normalized coordinate sets
   - Generate all unique orientations (rotation + reflection)
   - Cache orientations across regions for performance

### Key Insights

1. **Input Structure**: The actual input has a binary gap distribution:
   - 586 regions: negative gap (impossible)
   - 414 regions: gap ≥ 385 cells (trivially solvable with greedy)
   - 0 regions: small positive gaps (would require DLX)

2. **Algorithm Selection**: The minimum gap of 385 cells is huge compared to shape sizes (5-7 cells). With this much slack, greedy placement always succeeds.

3. **Performance**: The hybrid approach runs in **11 seconds** for all 1000 regions:
   - 586 impossible regions: instant (area check)
   - 414 possible regions: ~0.016s each (greedy placement)

4. **DLX Still Needed**: The example test cases have small gaps where greedy might fail, so DLX is retained for those cases.

## Test Cases

All tests in [test.py](test.py):
- Example case: 3 regions, expect 2 can fit (uses DLX for tight fit)
- Single shape fits: 4×4 grid with two 7-cell shapes (uses DLX)
- Single shape doesn't fit: 3×3 grid with 7-cell shape (area check)
- Rotation needed: verifies shape rotation/flip works

## Results

**Part 1**: 414 regions can fit all their presents (out of 1000 total)

**Part 2**: ⭐ (narrative conclusion - no computation required)

## Running Instructions

```bash
# Run solution
mise run solve 12 1
# or
python3 part_1.py inputs.txt

# Run tests
mise run test 12
# or
python3 test.py
```

## Performance

- Total execution time: **11 seconds**
- Regions processed: 1000
- Greedy placements: 414 regions (avg 0.016s each)
- Immediate failures: 586 regions (area check)
