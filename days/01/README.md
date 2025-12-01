# Day 1: Secret Entrance

## Problem Summary

The puzzle involves simulating a safe dial with positions 0-99. Starting at position 50, we follow a series of rotation instructions (L for left, R for right).

- **Part 1**: Count how many times the dial lands on position 0 after a rotation
- **Part 2**: Count how many times the dial passes through position 0 (during or after a rotation)

## Solution Approach

### Part 1 ([part_1.py](part_1.py))
The solution uses modulo arithmetic to handle the circular nature of the dial:
- **Left rotation**: `position = (position - distance) % 100`
- **Right rotation**: `position = (position + distance) % 100`
- Count only when the dial ends at position 0 after a complete rotation

The modulo operation ensures proper wrapping at the boundaries (0 ↔ 99).

### Part 2 ([part_2.py](part_2.py))
For each rotation, iterate through every click and check if it lands on 0:
- For left rotation: Check positions `(position - 1) % 100`, `(position - 2) % 100`, ..., `(position - distance) % 100`
- For right rotation: Check positions `(position + 1) % 100`, `(position + 2) % 100`, ..., `(position + distance) % 100`
- Count every instance where the dial points at 0

This brute-force approach is straightforward and handles all edge cases correctly. While not optimized for very large distances, it completes quickly enough for the puzzle input.

## Key Insights

1. **Circular arithmetic**: Using modulo 100 automatically handles wrapping in both directions
2. **State tracking**: Only need to track current position and count of zeros
3. **Part 2 complexity**: Need to detect passes through 0, not just ending at 0
4. **Edge cases**:
   - Wrapping from 0 going left → 99
   - Wrapping from 99 going right → 0
   - Multiple full rotations (e.g., R1000 passes through 0 ten times)
   - Exact 100-click rotations (R100 or L100 passes through 0 exactly once)

## Test Cases

### Part 1
- Example from puzzle: 10 rotations → 3 zeros

### Part 2
- Example from puzzle: 10 rotations → 6 zeros (3 at end + 3 during)
- Single rotation to zero: R50 → 1 zero
- Multiple wraps: R1000 → 10 zeros (10 complete circles)
- Pass through during rotation: L60 → 1 zero (50→...→0→...→90)
- No zeros: R10, L5, R3 → 0 zeros
- Exact wrap: R100 → 1 zero (completes one full circle)

## Results

**Part 1**: 1105
**Part 2**: 6599

## Running the Solution

```bash
# Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Uses custom input

# Part 2
python3 part_2.py              # Uses input.txt
python3 part_2.py --debug      # Debug with example data
python3 part_2.py custom.txt   # Uses custom input

# Run tests
python3 test.py
```
