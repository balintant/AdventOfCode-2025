# Day 2: Gift Shop

## Problem Summary

The puzzle involves identifying "invalid product IDs" in a gift shop database. An invalid product ID is a number that consists of a sequence of digits repeated exactly twice.

- **Part 1**: Find all invalid product IDs in given ranges and return their sum

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

## Key Insights

1. **String Pattern Matching**: Converting to string makes it easy to detect repeated patterns
2. **Even Length Requirement**: A number can only be a repeated pattern if it has even length
3. **Leading Zero Constraint**: The problem states numbers can't have leading zeros, so "0101" isn't valid
4. **Input Format**: Ranges are comma-separated on a single line, not newline-separated
5. **Examples of Invalid IDs**:
   - `11` = "1" repeated
   - `1010` = "10" repeated
   - `123123` = "123" repeated
   - `1188511885` = "11885" repeated

## Test Cases

### Part 1

- **Example from puzzle**: 11 ranges → sum = 1,227,775,554
  - Includes: 11, 22, 99, 1010, 222222, 446446, 1188511885, 38593859
- **Single range (10-20)**: Contains 11 → sum = 11
- **No invalid IDs (100-110)**: No repeated patterns → sum = 0
- **Multiple invalid (10-100)**: Contains 11, 22, 33, ..., 99 → sum = 495
- **Individual ID checks**: Verified is_invalid_id() correctly identifies patterns

## Results

**Part 1**: 29940924880

## Running the Solution

```bash
# Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Uses custom input

# Run tests
python3 test.py
```
