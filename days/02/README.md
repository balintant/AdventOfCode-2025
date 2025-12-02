# Day 2: Gift Shop

## Problem Summary

The puzzle involves identifying "invalid product IDs" in a gift shop database.

- **Part 1**: An invalid product ID is a number that consists of a sequence of digits repeated exactly twice
- **Part 2**: An invalid product ID is a number that consists of a sequence of digits repeated at least twice (2 or more times)

## Solution Approach

### Part 1 ([part_1.py](part_1.py))

The solution uses string manipulation to detect repeated patterns:

1. **Pattern Detection**: Convert the number to a string and check if it has even length
2. **Split and Compare**: Split the string in half and check if both halves are identical
3. **Leading Zero Check**: Ensure the first half doesn't start with '0' (numbers can't have leading zeros)
4. **Range Processing**: For each range, iterate through all numbers and sum the invalid IDs

**Algorithm:**
```python
def is_invalid_id(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False

    half_len = len(num_str) // 2
    first_half = num_str[:half_len]
    second_half = num_str[half_len:]

    return first_half == second_half and first_half[0] != '0'
```

**Time Complexity**: O(n × m) where n is the total numbers in all ranges and m is the average number of digits

### Part 2 ([part_2.py](part_2.py))

Part 2 extends the pattern detection to find sequences repeated 2 or more times:

1. **Try All Pattern Lengths**: For each possible pattern length from 1 to length÷2
2. **Check Divisibility**: Only check patterns where the total length is divisible by pattern length
3. **Pattern Reconstruction**: Repeat the pattern and check if it matches the entire number
4. **Leading Zero Check**: Ensure the pattern doesn't start with '0'
5. **Minimum Repetitions**: Only count if the pattern repeats at least 2 times

**Algorithm:**
```python
def is_invalid_id(num):
    num_str = str(num)
    length = len(num_str)

    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = num_str[:pattern_len]
            if pattern[0] == '0':
                continue

            num_repetitions = length // pattern_len
            if pattern * num_repetitions == num_str and num_repetitions >= 2:
                return True

    return False
```

**Key Difference**: Part 2 finds patterns like `111` (1 repeated 3x), `565656` (56 repeated 3x), and `2121212121` (21 repeated 5x), which Part 1 would miss.

**Time Complexity**: O(n × m²) where n is the total numbers in all ranges and m is the average number of digits

## Key Insights

1. **String Pattern Matching**: Converting to string makes it easy to detect repeated patterns
2. **Part 1 vs Part 2**: Part 1 only finds patterns repeated exactly 2 times (even length requirement), Part 2 finds any repetition count ≥ 2
3. **Leading Zero Constraint**: The problem states numbers can't have leading zeros, so "0101" isn't valid
4. **Input Format**: Ranges are comma-separated on a single line, not newline-separated
5. **Examples of Invalid IDs**:
   - Part 1: `11`, `1010`, `123123`, `1188511885`
   - Part 2 (additional): `111`, `999`, `565656`, `824824824`, `2121212121`

## Test Cases

### Part 1

- **Example from puzzle**: 11 ranges → sum = 1,227,775,554
  - Includes: 11, 22, 99, 1010, 222222, 446446, 1188511885, 38593859
- **Single range (10-20)**: Contains 11 → sum = 11
- **No invalid IDs (100-110)**: No repeated patterns → sum = 0
- **Multiple invalid (10-100)**: Contains 11, 22, 33, ..., 99 → sum = 495
- **Individual ID checks**: Verified is_invalid_id() correctly identifies patterns

### Part 2

- **Example from puzzle**: 11 ranges → sum = 4,174,379,265
  - Part 1 IDs plus: 111, 999, 565656, 824824824, 2121212121
- **Triple pattern (110-112)**: Contains 111 (1 repeated 3 times) → sum = 111
- **Multiple repetitions (1-1000)**: Contains various 2x, 3x, 4x patterns → sum = 5,490
- **Pattern detection**: Verified patterns repeated 2, 3, 4, 5+ times are correctly identified

## Results

**Part 1**: 29940924880
**Part 2**: 48631958998

## Running the Solution

```bash
# Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Uses custom input

# Part 2
python3 part_2.py              # Uses input.txt
python3 part_2.py custom.txt   # Uses custom input

# Run tests
python3 test.py
```
