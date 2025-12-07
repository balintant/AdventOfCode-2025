# Day 7: Laboratories

## Problem Summary

This puzzle simulates tachyon beam behavior through a manifold with two different physics models:

**Part 1 - Classical Physics**: Multiple tachyon beams move downward through the grid. When a beam hits a splitter (`^`), it stops and creates two new beams (left and right). Count the total number of beam splits.

**Part 2 - Quantum Physics**: A single tachyon particle takes BOTH paths at each splitter (many-worlds interpretation). Each unique path through the manifold creates a separate timeline. Count the total number of timelines.

Key mechanics:
- Beam/particle starts at `S` and moves downward
- Empty space (`.`) allows passage
- Splitters (`^`) create branching:
  - Part 1: Stop beam, create two new beams
  - Part 2: Particle continues on both paths simultaneously

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

### Part 2 - [part_2.py](part_2.py)

The solution uses recursive path counting with memoization:

1. **Recursive DFS**: Starting from `S`, explore all possible paths through the grid
2. **Branching logic**:
   - At a splitter: count paths going left AND paths going right (both branches)
   - At empty space: continue straight down (one path)
3. **Base cases**:
   - Reached bottom of grid: 1 complete path
   - Out of bounds horizontally: 0 paths (invalid)
4. **Memoization**: Cache results for each `(row, col)` position to avoid recomputing paths

**Why memoization is critical**: Without it, the algorithm recomputes paths from the same position exponentially many times. With memoization, each position is computed only once.

**Time Complexity**: O(rows × cols) with memoization
**Space Complexity**: O(rows × cols) for memo table

## Key Insights

1. **Set-based tracking (Part 1)**: Using a set to track active beam positions naturally handles beam convergence
2. **Row-by-row vs recursive (Parts 1 & 2)**: Part 1 uses iterative row-by-row processing; Part 2 uses recursive path counting
3. **Counting vs path enumeration**: Part 1 counts split events; Part 2 counts complete paths (timelines)
4. **Memoization necessity**: Part 2 requires memoization for performance—without it, the algorithm is exponentially slow
5. **Boundary checking**: Both solutions handle out-of-bounds gracefully (Part 1: don't add to next row; Part 2: return 0 paths)

## Test Cases

### Part 1 Tests
- **Example case**: 15-row grid with complex splitting pattern → 21 splits
- **Single split**: One beam hitting one splitter → 1 split
- **Parallel beams**: One split creating two beams, each hitting another splitter → 3 splits
- **Converging beams**: Two beams converging on the same splitter → Counts as 1 split at convergence point
- **No splitters**: Beam passes through empty space → 0 splits

### Part 2 Tests
- **Example case**: Same 15-row grid → 40 timelines (unique paths)
- **Single split**: One splitter → 2 timelines (left path, right path)
- **Two sequential splitters**: Two levels of splitting → 4 timelines (2² paths)
- **No splitters**: Straight path down → 1 timeline

## Results

- **Part 1**: 1698
- **Part 2**: 95408386769474

## Running the Solution

Using mise tasks:
```bash
mise run solve 7      # Run both parts
mise run solve 7 1    # Run Part 1
mise run solve 7 2    # Run Part 2
mise run test 7       # Run tests
```

Direct Python execution:
```bash
python3 part_1.py           # Run Part 1 with input.txt
python3 part_2.py           # Run Part 2 with input.txt
python3 test.py             # Run all tests (both parts)
```
