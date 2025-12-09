# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Meta-Rule: Maintaining CLAUDE.md

**CRITICAL**: When the user asks you to fix an issue or change behavior:

1. ✅ **ALWAYS** update CLAUDE.md to prevent the issue from recurring
2. ✅ Add checks, reminders, or validation steps to relevant sections
3. ✅ Update templates, checklists, or best practices as needed
4. ✅ Make the fix systematic, not just a one-time correction
5. ❌ **NEVER** fix an issue without updating CLAUDE.md
6. ❌ **NEVER** assume the fix is complete until documentation is updated

**Examples:**
- User reports wrong year in URLs → Update template + checklist with CRITICAL reminders
- User reports missing README updates → Add explicit requirements to maintenance rules
- User reports incorrect file structure → Update all references and templates

**Remember:** Every fix should make future instances of Claude Code smarter. If you fix something without updating CLAUDE.md, it WILL happen again.

## Project Overview

This is an Advent of Code 2025 repository for solving daily programming challenges during December 2025.

## Repository Structure

This repository uses Python for solutions with the following structure:
- Each day has its own directory: `days/01/`, `days/02/`, etc.
- Each day's directory contains:
  - `INSTRUCTIONS.md` - The puzzle story and task description
  - Solution files (always two separate files):
    - `part_1.py` - Part 1 solution
    - `part_2.py` - Part 2 solution
  - `test.py` - Test suite with multiple test cases for both parts
  - `input.txt` - Actual puzzle input (user-specific)
  - `README.md` - Solution documentation and approach (MUST be kept in sync with code)

### Running Solutions

Using mise tasks (recommended):
```bash
mise run solve 1         # Run Day 1 both parts (outputs two lines)
mise run solve 1 1       # Run Day 1 Part 1 only
mise run solve 1 2       # Run Day 1 Part 2 only
mise run test 1          # Run tests for Day 1
```

Direct Python execution:
```bash
cd days/NN  # NN is the zero-padded day number (01, 02, etc.)

# Run solutions:
python3 part_1.py              # Run Part 1
python3 part_2.py              # Run Part 2
python3 part_1.py custom.txt   # Use custom input
python3 part_2.py | pbcopy     # Copy Part 2 answer to clipboard (macOS)

# Run tests:
python3 test.py                        # Runs all test cases with descriptive output
```

## Development Workflow

### Creating New Day Solutions

When implementing or testing solutions:
1. **Always create separate files from the start**: `part_1.py` and `part_2.py`
2. Each day's puzzle has two parts that build on each other
3. Part 2 is revealed only after completing Part 1
4. Implement Part 1 first, then add Part 2 when it's revealed
5. Input data is unique per user and should not be committed to public repositories
6. Test with provided example inputs before running on actual puzzle input

### Testing Approach

**IMPORTANT**: Tests should be in a separate `test.py` file that imports from both solution files.

- Create test functions for both Part 1 and Part 2 (e.g., `test_example_part1()`, `test_example_part2()`)
- Add test functions for edge cases (wrap-around, boundary conditions, etc.)
- Each test should have descriptive names and inline comments explaining the test case
- Use assertions to verify expected results
- Include a `run_tests()` function that runs all test functions sequentially

**Import pattern:**
```python
from part_1 import solve as solve_part1
from part_2 import solve as solve_part2
```

### Problem-Solving Protocol

**CRITICAL**: Before writing any code:

1. **Read instructions completely**:
   - Read the entire INSTRUCTIONS.md file carefully
   - Note any hyperlinks or references to other problems/resources
   - Use WebFetch to retrieve and understand any linked content
   - The linked content may contain crucial context, special rules, or problem constraints

2. **Understand the problem deeply**:
   - Work through the provided example by hand
   - Verify your understanding matches the expected output
   - Identify edge cases and special conditions
   - Never assume - if something is unclear, investigate thoroughly

3. **Validate with examples first**:
   - Always test against the provided example before running on actual input
   - If the example fails, your understanding or implementation is wrong
   - Debug with small, simple test cases first

4. **When an answer is rejected**:
   - "Too low" or "Too high" means your logic has a bug
   - Re-read the instructions - you may have missed a detail
   - Check if you're processing all the data
   - Verify your parsing is correct
   - Test with hand-calculated examples

### Debugging Structured Text and Whitespace-Sensitive Problems

**CRITICAL**: When dealing with problems involving columns, positions, alignment, or any whitespace-dependent structure:

**Core Principle: Inspect Before Reasoning**
- **Never reason about whitespace you cannot see**
- Your mental model may trim or collapse spaces automatically
- Always write code to make whitespace visible BEFORE implementing logic

**Red Flags** (trigger this protocol immediately):
- Words like "column", "position", "aligned", "vertical", "spacing"
- Example outputs that show specific character positions
- Problems where spaces are part of the data structure (not just delimiters)
- Any time parsing "fails" but you can't see why

**Mandatory First Step - Make Structure Visible:**

```python
# WRONG: Trying to understand structure from visual inspection
# You cannot trust your mental representation of whitespace

# RIGHT: Make whitespace explicit with code
print("=== STRUCTURE INSPECTION ===")
for i, line in enumerate(lines):
    print(f'{i}: |{line}| len={len(line)}')
    for j, char in enumerate(line):
        print(f'  [{j}]="{char}" (ord={ord(char)})')
```

**After 2-3 Failed Attempts:**
1. STOP trying new algorithms
2. Write inspection code (as above)
3. Show output to user
4. Ask: "Does this match what you see?"
5. Only proceed after confirming your view matches reality

**Character-by-Character Debugging Pattern:**

```python
# When columns/positions matter, show exact character positions
test_data = """ABC  DEF
GHI   JK
+    *  """

print("Character grid:")
for row_idx, line in enumerate(test_data.split('\n')):
    print(f"Row {row_idx}:")
    for col_idx, char in enumerate(line):
        print(f"  [{col_idx}] = '{char}' (space={char == ' '})")
```

**Verification Checklist:**
- ✅ Can you see every space character explicitly?
- ✅ Do you know the exact length of each line?
- ✅ Can you point to specific character indices?
- ✅ Have you verified trailing/leading spaces are preserved?
- ❌ Are you assuming alignment based on visual appearance?
- ❌ Are you using split() when character positions matter?

**Common Mistakes:**
1. Using `split()` when exact positions matter (split() removes spacing information)
2. Using `strip()` on lines that need trailing spaces preserved
3. Assuming visual alignment in markdown/terminal matches actual characters
4. Reasoning about "columns" without verifying character indices

**Recovery Protocol:**
1. Write code to dump structure with delimiters: `|{line}|`
2. Show character-by-character breakdown with indices
3. Verify with user that your view matches theirs
4. Only then implement parsing logic
5. Test on simplest possible example first

**Example - Day 6 Learning:**
- Problem involved character columns where spacing was structural
- Initial attempts failed because whitespace wasn't visible in mental model
- Solution: Explicit character position inspection revealed the true structure
- Lesson: Code-first debugging for whitespace > visual reasoning

### Common Patterns

- Parse input data carefully (mind trailing newlines, number formatting)
- Many puzzles involve grid/graph traversal, pathfinding, or dynamic programming
- Consider performance for larger inputs (some puzzles require optimization)
- Part 2 often requires rethinking Part 1's approach for efficiency
- **When instructions reference external links, those links often contain critical information**

### Algorithmic Optimization and Performance

**CRITICAL**: When a solution times out or is too slow, STOP and re-think the approach. Advent of Code solutions should run in seconds, not minutes.

**Red Flags** (indicates you need a better algorithm):
- Solution takes >30 seconds to run
- You're iterating through ranges of 10,000+ consecutive integers
- You're checking every point in a large coordinate space
- You're doing O(n³) or worse operations on large inputs
- User says "this should be simple" or "there must be a mathematical solution"

**Key Insight: Sparse vs Dense Data**
- **Sparse data**: Few actual data points in a huge coordinate space (e.g., 500 points in a 100,000×100,000 grid)
- **Dense data**: Most coordinates contain data
- **If sparse, work ONLY with the actual data points, not the entire coordinate space**

**Example - Day 9 Learning:**
- **Problem**: 496 red tiles with coordinates up to ~98,000
- **Naive approach**: Check every integer y-coordinate from 0 to 98,000 → Times out
- **Optimized approach**: Only check the 496 y-coordinates where vertices exist → Completes in <30 seconds
- **Improvement**: 100× faster by recognizing sparse data structure

**Optimization Strategies:**

1. **Sparse Coordinate Processing**:
   - When coordinates are huge but data points are few, only process actual data points
   - Use sets/dicts for O(1) lookups instead of iterating through ranges
   - Example: Instead of `for y in range(0, 100000)`, use `for y in sorted(set(y for x, y in points))`

2. **Interval Arithmetic**:
   - Instead of checking every point in a range, check if entire intervals are valid
   - Merge/split intervals for efficient range operations
   - Example: Check if [x_min, x_max] is contained in union of intervals, not every x

3. **Scanline Algorithms**:
   - For 2D problems, process one row/column at a time
   - Build interval maps for fast lookups: y → x-ranges where condition is true
   - Useful for rectilinear polygons, filled regions, intersection problems

4. **Early Termination**:
   - Sort candidates by priority (e.g., largest first)
   - Return as soon as first valid solution is found
   - Check quick rejection conditions before expensive validation

5. **Pre-computation**:
   - Compute expensive structures once (edge lists, interval maps, lookup tables)
   - Use caching for repeated calculations
   - Balance pre-computation cost vs per-query cost

**When to Ask for Help:**
If you've tried multiple approaches and still timing out:
1. State what you've tried and why each failed
2. Explain the bottleneck (e.g., "checking 50,000 y-coordinates × 100,000 x-coordinates")
3. Ask user: "What mathematical property or algorithm am I missing?"

**Remember**: Part 2 is often VERY different from Part 1. Don't just optimize Part 1's approach—sometimes you need a completely different algorithm.

### File Structure Philosophy

**Always use split files:**
- Create `part_1.py` when implementing Part 1
- Create `part_2.py` when Part 2 is revealed
- This is the standard and only approach for this project

**Why split files:**
- Advent of Code puzzles always have two parts
- Part 2 often requires different logic or optimizations
- Cleaner separation of concerns
- Easier to run and test parts independently
- Aligns with mise task structure
- Each file has a single, clear responsibility

## Code Organization

### Solution Script Template

**Template for `part_1.py` and `part_2.py`:**

Each solution file should follow this structure:
1. Shebang line: `#!/usr/bin/env python3`
2. Docstring with day title, link, and **which part** this solves
   - **CRITICAL**: URL must use year 2025: `https://adventofcode.com/2025/day/N`
   - Format: `Day N: <Title> - Part X`
3. Import `sys` for command-line argument parsing
4. `solve(data)` function that takes input data directly (list, string, etc.)
   - Single `solve()` function per file (each file handles one part)
5. `solve_from_file(filename)` function to read and solve from a file
6. `main()` function that:
   - Parses command-line args (defaults to 'input.txt')
   - Solves puzzle with specified input file
   - **IMPORTANT**: Only prints the raw answer (no decorative output) to support piping (e.g., `python3 part_1.py | pbcopy`)
7. Guard: `if __name__ == '__main__':`

### Test Script Template

**Template for `test.py`:**

1. Shebang line: `#!/usr/bin/env python3`
2. Docstring describing the test suite
3. **Imports:**
   ```python
   from part_1 import solve as solve_part1
   from part_2 import solve as solve_part2
   ```
4. Multiple `test_*()` functions for different test cases:
   - `test_example_part1()` and `test_example_part2()` - examples from the puzzle
   - Additional tests for edge cases, clearly named by part (e.g., `test_edge_case_part2()`)
5. `run_tests()` function that runs all test functions with organized output (separate Part 1 and Part 2 sections)
6. Guard: `if __name__ == '__main__':`

### Best Practices

- Keep each day's solution self-contained within its directory
- Separate solution logic from tests (`test.py`)
- The `solve()` function should accept parsed data directly, not file paths
- The `solve_from_file()` function handles file I/O separately
- Accept command-line arguments for input file (default to 'input.txt')
- **Solution output**: Solution scripts print only the raw answer for easy piping (e.g., `python3 solution.py | pbcopy`)
- **Test output**: `test.py` prints descriptive messages with checkmarks (✓) for passing tests
- Write multiple test functions to cover edge cases for both parts
- Use inline comments in tests to show the transformation steps
- Use modulo arithmetic for circular/wrapping problems (e.g., `(position + offset) % max_value`)
- **IMPORTANT**: Only use Python standard library modules - no pip packages or external dependencies
- **CRITICAL**: When changing code structure (splitting files, changing function names, etc.), immediately update the day's README.md in the same session
- **Remove dead code**: After solving, review for unused functions created during exploration. Remove helper functions that duplicate logic or are never called.
- **Add validation**: When making assumptions about data structure (e.g., "crossings come in pairs"), add explicit validation with clear error messages. Fail fast with descriptive errors rather than silently producing wrong results.

### Documentation (README.md)

Each day's `README.md` should include:
1. **Problem Summary** - Brief description of the puzzle (both parts)
2. **Solution Approach** - Algorithm and data structures used (separate sections for Part 1 and Part 2)
   - Include links to solution files: `[part_1.py](part_1.py)` and `[part_2.py](part_2.py)`
   - Clearly explain any differences between Part 1 and Part 2 approaches
3. **Key Insights** - Important observations or techniques
4. **Test Cases** - Description of test cases and edge cases covered (for both parts)
5. **Results** - Final answers for Part 1 and Part 2
6. **Running Instructions** - Exact commands to run the solution (must match actual file names)

**The README.md must perfectly reflect the actual code structure and file names.**

## Documentation Maintenance

**CRITICAL**: Avoid redundant documentation. Each piece of information should exist in ONE authoritative location.

### Single Source of Truth

- **Tool versions and dependencies** → [mise.toml](mise.toml) only
- **VSCode extensions** → [.vscode/extensions.json](.vscode/extensions.json) only
- **VSCode settings** → [.vscode/settings.shared.json](.vscode/settings.shared.json) only
- **Running solutions** → Day's README.md and CLAUDE.md should reference mise tasks, not duplicate commands
- **Project structure** → README.md only
- **Code templates** → CLAUDE.md only
- **Daily solutions** → Day's README.md only

### When to Update Documentation

You MUST update relevant documentation files when making changes:

1. **Project-level changes** → Update [README.md](README.md):
   - Adding new capabilities or features
   - Modifying project structure
   - **Completing a day's solution** → Update the progress table with Part 1 and Part 2 answers
   - Changing file structure or naming conventions (e.g., switching to split files)
   - Modifying mise task commands or workflow
   - **Reference** other files (mise.toml, .vscode/*) rather than duplicating their content

2. **Day-level changes** → **ALWAYS** update `days/NN/README.md`:
   - **CRITICAL**: Any code changes to a day's solution MUST be reflected in that day's README.md
   - Implementing Part 2 of a puzzle (update solution approach, results, running instructions)
   - Optimizing the solution approach
   - Adding new test cases
   - Discovering new insights
   - Updating final answers
   - Changing file structure (e.g., splitting into `part_1.py` and `part_2.py`)
   - Modifying function signatures or interfaces
   - **Never leave README.md stale or inconsistent with the actual implementation**

   **Additional updates when creating/modifying solutions:**
   - Verify `mise run solve N 1` and `mise run solve N 2` work (N = day number, no zero-padding)
   - Update test.py imports to use the correct files
   - Test all commands documented in README.md
   - **CRITICAL**: Verify docstring URLs use correct year: `https://adventofcode.com/2025/day/N` (NOT 2024!)

3. **Workflow changes** → Update [CLAUDE.md](CLAUDE.md):
   - Modifying code templates or structure
   - Adding new best practices
   - Changing testing approaches
   - Updating development patterns
   - **CRITICAL**: When fixing ANY issue reported by the user → Update CLAUDE.md to prevent recurrence
   - Add validation steps, reminders, or checks to prevent the same issue in future sessions

### README.md Maintenance Rules

#### Day-level README.md (days/NN/README.md)

**The day's README.md is the single source of truth for that day's solution.** It must ALWAYS be kept in sync with the code.

When you make ANY change to a day's solution:
1. ✅ **DO**: Update the README.md immediately in the same session
2. ✅ **DO**: Verify that running instructions match the actual file names
3. ✅ **DO**: Update the solution approach if implementation changes
4. ✅ **DO**: Update results when you get new answers
5. ❌ **DON'T**: Leave README.md referencing files that don't exist
6. ❌ **DON'T**: Leave README.md with incorrect answers
7. ❌ **DON'T**: Leave README.md describing an approach that's not implemented

#### Project-level README.md (README.md)

**The project README.md must be updated when completing solutions.**

When you complete a day's solution (Part 1, Part 2, or both):
1. ✅ **DO**: Update the progress table with the correct answers
2. ✅ **DO**: Update status to ✅ when both parts are complete
3. ✅ **DO**: Update project structure if file organization changes
4. ✅ **DO**: Update running instructions if mise commands change
5. ❌ **DON'T**: Leave the progress table with "-" when you have answers
6. ❌ **DON'T**: Forget to update after solving Part 2

### Creating a New Day: Complete Checklist

When starting a new day's solution, follow this checklist:

**IMPORTANT:** Use TodoWrite to track this process and ensure nothing is missed!

**Required actions:**
1. ✅ Create day directory: `days/NN/` (NN = zero-padded day number: 01, 02, etc.)
2. ✅ Add `INSTRUCTIONS.md` with the puzzle description
   - **CRITICAL**: Read the INSTRUCTIONS.md completely and carefully
   - **CRITICAL**: Check for and follow any hyperlinks in the instructions (e.g., references to related problems, external resources)
   - **CRITICAL**: Use WebFetch to retrieve and understand any linked resources that might contain important context or rules
3. ✅ Create `part_1.py` with Part 1 logic and proper docstring
   - **CRITICAL**: Verify URL is `https://adventofcode.com/2025/day/N` (year 2025, NOT 2024!)
4. ✅ Create `test.py` with Part 1 tests using standard imports:
   ```python
   from part_1 import solve as solve_part1
   # from part_2 import solve as solve_part2  # Uncomment when Part 2 is ready
   ```
5. ✅ Add `input.txt` with your puzzle input
6. ✅ Create `README.md` documenting the solution
7. ✅ When Part 2 is revealed:
   - Create `part_2.py` with Part 2 logic
   - **CRITICAL**: Verify URL is `https://adventofcode.com/2025/day/N` (year 2025, NOT 2024!)
   - Uncomment Part 2 imports in `test.py`
   - Add Part 2 tests
   - Update `README.md` with Part 2 details
   - Update project `README.md` progress table with both Part 1 and Part 2 answers
8. ✅ Test everything:
   - Run `python3 test.py` to ensure all tests pass
   - Run `mise run solve 1 1` to verify Part 1 works (no zero-padding needed)
   - Run `mise run solve 1 2` to verify Part 2 works

**Note:** `mise.toml` automatically detects and supports both `part_N.py` files and unified `solution.py` with `solve_partN` functions.

### Documentation Update Process

When making changes:
1. **Identify** the single authoritative location for this information
2. **Update** only that location
3. **Reference** (don't duplicate) that location from other docs if needed
4. **Remove** any redundant copies of the same information
5. **Verify** that examples and instructions still work

### Examples

- ✅ Added tool dependency → Update mise.toml, reference it from README
- ❌ Added tool dependency → Update mise.toml AND copy version to README
- ✅ Changed VSCode extension → Update extensions.json
- ❌ Changed VSCode extension → Update extensions.json AND list it in README
- ✅ Solved Part 2 → Update day's README.md and project progress table
- ✅ Changed test approach → Update CLAUDE.md only

**Remember**: Documentation is code. Each fact should exist in exactly one place.
