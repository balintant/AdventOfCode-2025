# Day 6: Trash Compactor

## Problem Summary

The puzzle presents a unique format for math problems: they're arranged vertically in columns rather than horizontally. Each problem consists of numbers stacked vertically with an operator (`+` or `*`) at the bottom. Problems are separated by full columns of spaces. The task is to solve each problem and calculate the grand total by summing all individual problem results.

## Solution Approach

### Part 1

**Algorithm**: [part_1.py](part_1.py)

1. **Parse the worksheet**:
   - Split the last row to get the list of operators
   - Split each number row by whitespace to get lists of numbers
   - Each row contains numbers separated by spaces

2. **Match operators to numbers**:
   - The i-th operator corresponds to the i-th number in each row
   - For each operator position, collect the number at that position from all rows

3. **Calculate results**:
   - For addition (`+`): sum all numbers
   - For multiplication (`*`): multiply all numbers together

4. **Sum all results**: Add up all individual problem answers to get the grand total

**Key Insights**:
- Numbers and operators are separated by whitespace
- Split by spaces to parse both operators and numbers
- Match by position: i-th operator uses i-th number from each row
- Simple sequential processing - no need for column position tracking

**Test Cases**:
- Example from puzzle: 4 problems resulting in grand total of 4,277,556
- Single addition: Simple vertical addition test
- Single multiplication: Simple vertical multiplication test
- Two problems: Multiple problems separated by space columns

## Results

**Part 1**: `5171061464548`

**Part 2**: Not yet revealed

## Running Instructions

```bash
# Run Part 1
python3 part_1.py              # Uses input.txt by default
python3 part_1.py custom.txt   # Use custom input file

# Run tests
python3 test.py

# Using mise
mise run solve 6 1   # Run Part 1
mise run test 6      # Run tests
```
