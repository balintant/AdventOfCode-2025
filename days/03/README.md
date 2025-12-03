# Day 3: Lobby

## Problem Summary

The puzzle involves finding maximum joltage from battery banks to power an escalator.

- **Part 1**: Each bank is a string of digits (1-9). Select exactly 2 batteries to form a 2-digit number. Find the maximum possible for each bank and sum them.

## Solution Approach

### Part 1 ([part_1.py](part_1.py))

The solution tries all possible pairs of batteries in each bank:

1. **Pair Generation**: For each bank, generate all pairs (i, j) where i < j
2. **Joltage Calculation**: Form a 2-digit number by concatenating digits at positions i and j
3. **Maximum Selection**: Find the maximum joltage from all pairs
4. **Summation**: Sum the maximum joltages from all banks

**Algorithm:**
```python
def find_max_joltage(bank):
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage
```

**Key Insight**: We can pick ANY two batteries from the bank, not just consecutive ones. The order is preserved (can't rearrange), so picking batteries at positions i and j (i < j) gives us the digit at position i followed by the digit at position j.

**Time Complexity**: O(n × m²) where n is the number of banks and m is the average length of each bank

## Key Insights

1. **Order Preservation**: Batteries cannot be rearranged - if we pick positions i and j, the result is digits[i] + digits[j]
2. **Non-Consecutive Selection**: We can pick any two batteries, not just adjacent ones
3. **Optimization**: For maximum joltage, ideally we want the highest digit in the tens place and the second-highest in the ones place
4. **Examples**:
   - `987654321111111` → Pick positions 0,1 → `98`
   - `811111111111119` → Pick positions 0,14 → `89` (8 at start, 9 at end)
   - `234234234234278` → Pick positions 12,13 → `78` (last two digits)
   - `818181911112111` → Pick positions 6,7 → `92` (9 and 2 from middle)

## Test Cases

### Part 1

- **Example from puzzle**: 4 banks → sum = 357
  - `987654321111111` → 98
  - `811111111111119` → 89
  - `234234234234278` → 78
  - `818181911112111` → 92
- **Single bank**: `987654321` → 98
- **All same digits**: `11111` → 11, `99999` → 99
- **Ascending/Descending**: `123456789` → 89, `987654321` → 98

## Results

**Part 1**: 17443

## Running the Solution

```bash
# Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Uses custom input

# Run tests
python3 test.py
```
