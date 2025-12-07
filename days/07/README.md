# Day 7: Laboratories

## Problem Summary

This puzzle simulates tachyon beam splitting through a manifold. A tachyon beam starts at position `S` and moves downward through a grid. When it encounters a splitter (`^`), the beam stops and two new beams are emitted from the immediate left and right of the splitter, continuing downward. The goal is to count the total number of beam splits.

Key mechanics:
- Beam starts at `S` and moves downward
- Empty space (`.`) allows beams to pass through
- Splitters (`^`) stop the incoming beam and create two new beams (left and right)
- Multiple beams can converge on the same position
- Count each time a beam hits a splitter (total number of splits)

## Solution Approach

### Part 1 - [part_1.py](part_1.py)

The solution uses a simulation approach that processes the grid row by row:

1. **Find starting position**: Locate the `S` in the top row
2. **Track active beams**: Use a set to track column positions of active beams for each row
3. **Process each row**:
   - For each active beam position, check what it hits in the current row
   - If it hits empty space (`.`), the beam continues to the same column in the next row
   - If it hits a splitter (`^`):
     - Increment the split counter
     - Create two new beams at positions `col-1` and `col+1`
4. **Handle convergence**: Using a set automatically handles multiple beams converging on the same position

**Time Complexity**: O(rows × beams_per_row)
**Space Complexity**: O(max_beams_active)

## Key Insights

1. **Set-based tracking**: Using a set to track active beam positions naturally handles beam convergence (multiple beams at the same position only create one beam continuation)
2. **Row-by-row simulation**: Processing the grid top-to-bottom matches the physical behavior of downward-moving beams
3. **Counting splits, not beams**: The answer is the total number of split events, not the number of beams created
4. **Boundary checking**: Beams that would go outside the grid boundaries are simply not added to the next row's active set

## Test Cases

All test cases validate the beam splitting logic:

- **Example case**: 15-row grid with complex splitting pattern → 21 splits
- **Single split**: One beam hitting one splitter → 1 split
- **Parallel beams**: One split creating two beams, each hitting another splitter → 3 splits
- **Converging beams**: Two beams converging on the same splitter → Counts as 1 split at convergence point
- **No splitters**: Beam passes through empty space → 0 splits

## Results

- **Part 1**: 1698

## Running the Solution

Using mise tasks:
```bash
mise run solve 7 1    # Run Part 1
mise run test 7       # Run tests
```

Direct Python execution:
```bash
python3 part_1.py           # Run Part 1 with input.txt
python3 test.py             # Run all tests
```
