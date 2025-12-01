# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Advent of Code 2025 repository for solving daily programming challenges during December 2025.

## Repository Structure

This repository uses Python for solutions with the following structure:
- Each day has its own directory: `days/01/`, `days/02/`, etc.
- Each day's directory contains:
  - `INSTRUCTIONS.md` - The puzzle story and task description
  - `solution.py` - Python solution script (core logic only)
  - `test.py` - Test suite with multiple test cases
  - `input.txt` - Actual puzzle input (user-specific)
  - `README.md` - Solution documentation and approach

### Running Solutions

To run a day's solution:
```bash
cd days/NN  # NN is the zero-padded day number (01, 02, etc.)
python3 solution.py              # Uses input.txt by default, outputs raw answer
python3 solution.py custom.txt   # Uses specified input file
python3 solution.py | pbcopy     # Copy answer to clipboard (macOS)
```

To run tests:
```bash
cd days/NN
python3 test.py                  # Runs all test cases with descriptive output
```

## Development Workflow

### Creating New Day Solutions

When implementing or testing solutions:
1. Each day's puzzle has two parts that build on each other
2. Part 2 is revealed only after completing Part 1
3. Input data is unique per user and should not be committed to public repositories
4. Test with provided example inputs before running on actual puzzle input

### Testing Approach

**IMPORTANT**: Tests should be in a separate `test.py` file that imports from `solution.py`.

- Create a `test_example()` function with the example from the puzzle description
- Add test functions for edge cases (wrap-around, boundary conditions, etc.)
- Each test should have descriptive names and inline comments explaining the test case
- Use assertions to verify expected results
- Include a `run_tests()` function that runs all test functions sequentially
- Tests import the `solve()` function from the solution module

### Common Patterns

- Parse input data carefully (mind trailing newlines, number formatting)
- Many puzzles involve grid/graph traversal, pathfinding, or dynamic programming
- Consider performance for larger inputs (some puzzles require optimization)
- Part 2 often requires rethinking Part 1's approach for efficiency

## Code Organization

### Solution Script Template

Each `solution.py` should follow this structure:
1. Shebang line: `#!/usr/bin/env python3`
2. Docstring with day title, link, and task summary
3. Import `sys` for command-line argument parsing
4. `solve(data)` function that takes input data directly (list, string, etc.)
5. `solve_from_file(filename)` function to read and solve from a file
6. `main()` function that:
   - Parses command-line args (defaults to 'input.txt')
   - Solves puzzle with specified input file
   - **IMPORTANT**: Only prints the raw answer (no decorative output) to support piping (e.g., `python3 solution.py | pbcopy`)
7. Guard: `if __name__ == '__main__':`

### Test Script Template

Each `test.py` should follow this structure:
1. Shebang line: `#!/usr/bin/env python3`
2. Docstring describing the test suite
3. Import statement: `from solution import solve`
4. Multiple `test_*()` functions for different test cases:
   - `test_example()` - the example from the puzzle
   - Additional tests for edge cases
5. `run_tests()` function that runs all test functions
6. Guard: `if __name__ == '__main__':`

### Best Practices

- Keep each day's solution self-contained within its directory
- Separate solution logic (`solution.py`) from tests (`test.py`)
- The `solve()` function should accept parsed data directly, not file paths
- The `solve_from_file()` function handles file I/O separately
- Accept command-line arguments for input file (default to 'input.txt')
- **Solution output**: `solution.py` prints only the raw answer for easy piping (e.g., `python3 solution.py | pbcopy`)
- **Test output**: `test.py` prints descriptive messages with checkmarks (✓) for passing tests
- Write multiple test functions to cover edge cases
- Use inline comments in tests to show the transformation steps
- Use modulo arithmetic for circular/wrapping problems (e.g., `(position + offset) % max_value`)
- **IMPORTANT**: Only use Python standard library modules - no pip packages or external dependencies

### Documentation (README.md)

Each day's `README.md` should include:
1. **Problem Summary** - Brief description of the puzzle
2. **Solution Approach** - Algorithm and data structures used
3. **Key Insights** - Important observations or techniques
4. **Test Cases** - Description of test cases and edge cases covered
5. **Results** - Final answers for Part 1 (and Part 2 when available)
6. **Running Instructions** - How to run the solution

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
   - Changing the progress table
   - **Reference** other files (mise.toml, .vscode/*) rather than duplicating their content

2. **Day-level changes** → Update `days/NN/README.md`:
   - Implementing Part 2 of a puzzle
   - Optimizing the solution approach
   - Adding new test cases
   - Discovering new insights
   - Updating final answers

3. **Workflow changes** → Update [CLAUDE.md](CLAUDE.md):
   - Modifying code templates or structure
   - Adding new best practices
   - Changing testing approaches
   - Updating development patterns

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
