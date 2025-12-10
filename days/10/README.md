# Day 10: Factory

## Problem Summary

This puzzle involves configuring indicator lights on factory machines. Each machine has:
- A set of indicator lights (initially all off)
- A target configuration (some lights on, some off)
- Multiple buttons that toggle specific lights

The goal is to find the minimum number of button presses needed to configure all machines correctly.

## Solution Approach

### Part 1

This is a classic "lights out" problem that can be solved using linear algebra over GF(2) (the binary field). See [part_1.py](part_1.py) for the implementation.

**Key insights:**

1. **Binary Toggle Logic**: Each button toggles specific lights. Pressing a button twice returns lights to their original state, so we only care about pressing each button 0 or 1 times (mod 2).

2. **Linear System**: For each machine:
   - Variables: whether each button is pressed (0 or 1)
   - Equations: for each light, the XOR of all buttons affecting it must equal the target state
   - This forms a system of linear equations over GF(2)

3. **Gaussian Elimination**: We use reduced row echelon form (RREF) to:
   - Identify pivot variables (dependent on other variables)
   - Identify free variables (can be set independently)
   - Check for inconsistency (no solution exists)

4. **Optimization**: When free variables exist (underdetermined system), we enumerate all combinations to find the solution with minimum button presses.

**Algorithm:**
```
For each machine:
  1. Build coefficient matrix: matrix[light][button] = 1 if button affects light
  2. Convert to RREF using Gaussian elimination over GF(2)
  3. Identify free variables (columns without pivots)
  4. If no free variables: return the unique solution
  5. Otherwise: try all 2^k combinations of free variable values
  6. Return the solution with minimum sum (fewest button presses)
Sum all machine results
```

**Time Complexity**: O(n³ + 2^f) per machine, where:
- n = max(lights, buttons) for Gaussian elimination
- f = number of free variables for optimization

For the input data, f is typically small (0-3), making enumeration feasible.

## Test Cases

The puzzle provides three example machines:
- Machine 1: `[.##.]` with 6 buttons → 2 presses minimum
- Machine 2: `[...#.]` with 5 buttons → 3 presses minimum
- Machine 3: `[.###.#]` with 4 buttons → 2 presses minimum
- Total: 7 presses

Additional tests verify each machine individually to ensure correct parsing and solving.

## Results

- **Part 1**: 432 button presses

## Running the Solution

```bash
# Run Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Use custom input

# Run tests
python3 test.py

# Using mise
mise run solve 10 1            # Run Part 1
mise run test 10               # Run tests
```
