# Day 1: Secret Entrance

## Problem Summary

The puzzle involves simulating a safe dial with positions 0-99. Starting at position 50, we follow a series of rotation instructions (L for left, R for right) and count how many times the dial lands on position 0.

## Solution Approach

The solution uses modulo arithmetic to handle the circular nature of the dial:
- **Left rotation**: `position = (position - distance) % 100`
- **Right rotation**: `position = (position + distance) % 100`

The modulo operation ensures proper wrapping at the boundaries (0 ↔ 99).

## Key Insights

1. **Circular arithmetic**: Using modulo 100 automatically handles wrapping in both directions
2. **State tracking**: Only need to track current position and count of zeros
3. **Edge cases**:
   - Wrapping from 0 going left → 99
   - Wrapping from 99 going right → 0
   - Multiple full rotations (distance > 100)

## Test Cases

- Example from puzzle: 10 rotations → 3 zeros
- Single rotation to zero: R50 → 1 zero
- Wrap around left: L50, L1 → 1 zero (50→0→99)
- Wrap around right: R49, R1 → 1 zero (50→99→0)
- No zeros: R10, L5, R3 → 0 zeros
- Multiple zeros: L50, R100, L100 → 3 zeros

## Results

**Part 1**: 1105

## Running the Solution

```bash
# Run with default input.txt
python3 solution.py

# Run with custom input
python3 solution.py custom_input.txt
```
