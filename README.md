# Advent of Claude 2025

A collection of solutions for the [Advent of Code 2025](https://adventofcode.com/2025) programming challenges, solved using **pure vibe coding** with Claude Code.

## What is Pure Vibe Coding?

This repository is an experiment in AI-assisted development where **all code is written by Claude Code with zero manual edits**. Every solution, test, and documentation file is generated through natural language interaction with Claude Code, demonstrating the power of AI-powered development workflows.

## Project Structure

```
AdventOfClaude-2025/
├── README.md           # This file
├── CLAUDE.md           # Instructions for Claude Code instances
├── mise.toml           # Tool versions and task definitions
└── days/               # All daily solutions
    ├── 01/             # Day 1 puzzle solution
    │   ├── INSTRUCTIONS.md    # Puzzle description
    │   ├── part_1.py          # Part 1 solution
    │   ├── part_2.py          # Part 2 solution
    │   ├── test.py            # Test suite
    │   ├── input.txt          # Puzzle input (user-specific)
    │   └── README.md          # Solution documentation
    ├── 02/             # Day 2 puzzle solution
    │   └── ...
    └── ...
```

Each day's directory contains:
- **INSTRUCTIONS.md** - The puzzle story and task description from Advent of Code
- **part_1.py** - Part 1 solution that prints only the raw answer (for easy piping)
- **part_2.py** - Part 2 solution that prints only the raw answer (for easy piping)
- **test.py** - Comprehensive test suite with example cases and edge cases
- **input.txt** - Personal puzzle input from Advent of Code
- **README.md** - Documentation of the approach, insights, and results

## Running Solutions

### Using mise (recommended)

```bash
# Run all parts for a day
mise run solve 1

# Run specific part
mise run solve 1 1      # Part 1
mise run solve 1 2      # Part 2

# Run tests
mise run test 1         # Test specific day
mise run test           # Test all days
```

### Direct Python execution

Navigate to any day's directory and run:

```bash
# Navigate to a specific day (zero-padded)
cd days/01

# Run solutions (outputs raw answer)
python3 part_1.py
python3 part_2.py

# Copy answer directly to clipboard (macOS)
python3 part_2.py | pbcopy

# Run with custom input
python3 part_1.py custom_input.txt

# Run all tests
python3 test.py
```

## Development Approach

### Principles

1. **Pure AI Development** - No manual code edits; all changes through Claude Code
2. **Test-Driven** - Each solution includes comprehensive tests for edge cases
3. **Clean Output** - Solutions output only raw answers for easy automation
4. **Self-Contained** - Each day is independent with its own tests and documentation
5. **Documented** - Clear explanations of approach, insights, and key techniques

### Workflow

1. Add the day's `INSTRUCTIONS.md` with the puzzle description
2. Use Claude Code to implement the solution
3. Create comprehensive tests covering edge cases
4. Document the approach and insights in the day's README
5. Verify the solution produces the correct answer
6. Move to the next day's puzzle

### Code Quality

All solutions follow consistent patterns:
- Type hints for function parameters and return values
- Descriptive variable and function names
- Inline comments explaining non-obvious logic
- Separation of concerns (parsing, logic, I/O)
- Modular functions that can be tested independently

## Setup

### Prerequisites

1. **Install mise** - Tool version manager for Python and other dependencies
   ```bash
   curl https://mise.run | sh
   ```
   See [mise.jdx.dev](https://mise.jdx.dev) for other installation methods.

2. **Install dependencies** - All tools and versions are defined in [mise.toml](mise.toml)
   ```bash
   mise install
   ```

3. **VSCode (recommended)** - Open the project and search for `@recommended` in Extensions to install
   - Configuration is stored in [.vscode/settings.shared.json](.vscode/settings.shared.json)
   - Extensions listed in [.vscode/extensions.json](.vscode/extensions.json)

### Quick Start

```bash
# Clone and setup
git clone https://github.com/balintant/AdventOfClaude-2025
cd AdventOfClaude-2025
mise install

# Run a day's solution
mise run solve 01

# Run tests for a specific day
mise run test 01

# Run all tests
mise run test
```

## Technologies

- **Tool Management**: [mise](https://mise.jdx.dev) - See [mise.toml](mise.toml) for versions
- **Language**: Python 3.13 (standard library only, no external dependencies)
- **IDE**: VSCode with Claude Code extension
- **AI Assistant**: Claude (Sonnet 4.5)
- **Testing**: Custom test functions with assertions
- **Linting**: Ruff

## Why This Matters

This project demonstrates:
- The capability of AI assistants to write production-quality code
- Effective human-AI collaboration through natural language
- The importance of good prompts and clear communication
- How AI can maintain consistency across a multi-day project
- The viability of "vibe coding" for solving algorithmic challenges

## Progress

| Day | Status | Part 1 | Part 2 |
|-----|--------|--------|--------|
| 1   | ✅     | 1105   | 6599   |
| 2   | ✅     | 29940924880 | 48631958998 |
| ... | -      | -      | -      |

## About Advent of Code

[Advent of Code](https://adventofcode.com) is an annual event featuring daily programming puzzles throughout December. Each day presents a two-part challenge that requires algorithmic thinking, problem-solving skills, and code implementation.

## License

This project is for educational and demonstration purposes. Puzzle descriptions and stories are © [Advent of Code](https://adventofcode.com).

## Acknowledgments

- **Eric Wastl** for creating Advent of Code
- **Anthropic** for developing Claude and Claude Code
- The Advent of Code community for inspiration and support

---

**Note**: This repository showcases pure AI-assisted development. Every line of code, test, and documentation was generated by Claude Code without manual editing.
