#!/usr/bin/env python3
"""Day 12: Christmas Tree Farm - Part 1
https://adventofcode.com/2025/day/12

Count how many regions can fit all their required presents using Dancing Links (DLX).
"""

import sys


def parse_input(data):
    """Parse the input into shapes and regions."""
    lines = [line.rstrip("\n") for line in data.strip().split("\n")]

    shapes = {}
    regions = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Region definition: "WxH: q0 q1 q2 ..."
        if line and "x" in line and ":" in line:
            parts = line.split()
            if parts and "x" in parts[0]:
                first_part = parts[0].rstrip(":")
                dims = first_part.split("x")
                width, height = int(dims[0]), int(dims[1])
                quantities = [int(x) for x in parts[1:]]
                regions.append((width, height, quantities))
                i += 1
                continue

        # Shape definition: "N:"
        if line and ":" in line and "x" not in line:
            try:
                shape_idx = int(line.split(":")[0])
                shape_lines = []
                i += 1
                while i < len(lines) and lines[i] and ":" not in lines[i]:
                    shape_lines.append(lines[i])
                    i += 1
                shapes[shape_idx] = shape_lines
                continue
            except ValueError:
                pass

        i += 1

    return shapes, regions


def shape_to_coords(shape_lines):
    """Convert shape lines to set of (row, col) coordinates."""
    coords = set()
    for r, line in enumerate(shape_lines):
        for c, char in enumerate(line):
            if char == "#":
                coords.add((r, c))
    return coords


def normalize_coords(coords):
    """Normalize coordinates to start at (0, 0)."""
    if not coords:
        return set()
    min_r = min(r for r, _ in coords)
    min_c = min(c for _, c in coords)
    return {(r - min_r, c - min_c) for r, c in coords}


def rotate_90(coords):
    """Rotate coordinates 90 degrees clockwise."""
    return normalize_coords({(c, -r) for r, c in coords})


def flip_horizontal(coords):
    """Flip coordinates horizontally."""
    return normalize_coords({(r, -c) for r, c in coords})


def get_all_orientations(shape_lines):
    """Get all unique orientations (rotations and flips) of a shape."""
    coords = normalize_coords(shape_to_coords(shape_lines))
    orientations = set()

    current = coords
    for _ in range(4):
        orientations.add(frozenset(current))
        orientations.add(frozenset(flip_horizontal(current)))
        current = rotate_90(current)

    return [set(o) for o in orientations]


# Dancing Links (DLX) Implementation


class DLXNode:
    """Node in the dancing links matrix."""

    def __init__(self, column=None):
        self.left = self.right = self.up = self.down = self
        self.column = column
        self.row_id = None


class DLXColumn(DLXNode):
    """Column header node with size tracking."""

    def __init__(self, name, is_primary=True):
        super().__init__(self)
        self.column = self
        self.name = name
        self.size = 0
        self.is_primary = is_primary


class DLX:
    """Dancing Links solver for exact cover problems."""

    def __init__(self, primary_columns, secondary_columns=None):
        """Initialize DLX with primary and secondary column names.

        Primary columns must be covered exactly once.
        Secondary columns can be covered at most once (optional).
        """
        self.header = DLXColumn("header")
        self.columns = {}

        # Create all column headers in one circular list
        prev = self.header
        for col_name in primary_columns:
            col = DLXColumn(col_name, is_primary=True)
            self.columns[col_name] = col
            col.left = prev
            col.right = prev.right
            prev.right.left = col
            prev.right = col
            prev = col

        if secondary_columns:
            for col_name in secondary_columns:
                col = DLXColumn(col_name, is_primary=False)
                self.columns[col_name] = col
                col.left = prev
                col.right = prev.right
                prev.right.left = col
                prev.right = col
                prev = col

        self.solution = []

    def add_row(self, row_id, column_names):
        """Add a row to the matrix."""
        if not column_names:
            return

        nodes = []
        for col_name in column_names:
            col = self.columns[col_name]
            node = DLXNode(col)
            node.row_id = row_id

            # Insert into column
            node.up = col.up
            node.down = col
            col.up.down = node
            col.up = node
            col.size += 1

            nodes.append(node)

        # Link nodes horizontally
        for i in range(len(nodes)):
            nodes[i].left = nodes[i - 1]
            nodes[i].right = nodes[(i + 1) % len(nodes)]

    def cover(self, col):
        """Cover column (remove from header list)."""
        col.right.left = col.left
        col.left.right = col.right

        # Remove all rows in this column
        node = col.down
        while node != col:
            right = node.right
            while right != node:
                right.down.up = right.up
                right.up.down = right.down
                right.column.size -= 1
                right = right.right
            node = node.down

    def uncover(self, col):
        """Uncover column (restore to header list)."""
        # Restore all rows in this column
        node = col.up
        while node != col:
            left = node.left
            while left != node:
                left.column.size += 1
                left.down.up = left
                left.up.down = left
                left = left.left
            node = node.up

        col.right.left = col
        col.left.right = col

    def search(self, max_depth=300):
        """Search for exact cover using DLX algorithm with depth limit."""
        # Check if all primary columns are covered
        col = self.header.right
        all_primary_covered = True
        while col != self.header:
            if col.is_primary:
                all_primary_covered = False
                break
            col = col.right

        if all_primary_covered:
            return True  # All primary columns covered

        # Depth limit to prevent infinite search
        if len(self.solution) >= max_depth:
            return False

        # Choose primary column with minimum size (MRV heuristic)
        col = self.header.right
        min_col = None
        while col != self.header:
            if col.is_primary:
                if min_col is None or col.size < min_col.size:
                    min_col = col
            col = col.right

        if min_col is None:
            return True  # No primary columns left

        if min_col.size == 0:
            return False  # Primary column can't be covered

        # Cover this column
        self.cover(min_col)

        # Try each row in this column
        row = min_col.down
        while row != min_col:
            self.solution.append(row.row_id)

            # Cover all columns in this row
            node = row.right
            while node != row:
                self.cover(node.column)
                node = node.right

            # Recursive search
            if self.search(max_depth):
                return True

            # Backtrack: uncover all columns in this row
            node = row.left
            while node != row:
                self.uncover(node.column)
                node = node.left

            self.solution.pop()
            row = row.down

        # Uncover column
        self.uncover(min_col)
        return False


def can_fit_greedy(
    width, height, quantities, shape_definitions, orientations_cache=None
):
    """Check if shapes fit using greedy placement (fast for large gaps)."""
    # Build list of shapes to place
    shapes_to_place = []
    for shape_idx, count in enumerate(quantities):
        for _ in range(count):
            shapes_to_place.append(shape_idx)

    if not shapes_to_place:
        return True

    # Quick area check
    total_area = sum(
        len(shape_to_coords(shape_definitions[shape_idx]))
        for shape_idx in shapes_to_place
    )
    if total_area > width * height:
        return False

    # Use cached orientations or compute them
    if orientations_cache:
        all_orientations = orientations_cache
    else:
        all_orientations = {}
        for shape_idx in set(shapes_to_place):
            all_orientations[shape_idx] = get_all_orientations(
                shape_definitions[shape_idx]
            )

    # Grid to track occupied cells
    grid = [[False] * width for _ in range(height)]

    # Try to place each shape greedily
    for shape_idx in shapes_to_place:
        placed = False
        for orientation in all_orientations[shape_idx]:
            if placed:
                break
            for start_r in range(height):
                if placed:
                    break
                for start_c in range(width):
                    # Check if shape fits at this position
                    valid = True
                    cells = []
                    for dr, dc in orientation:
                        r, c = start_r + dr, start_c + dc
                        if r < 0 or r >= height or c < 0 or c >= width or grid[r][c]:
                            valid = False
                            break
                        cells.append((r, c))

                    if valid:
                        # Place it
                        for r, c in cells:
                            grid[r][c] = True
                        placed = True
                        break

        if not placed:
            return False

    return True


def can_fit_region_dlx(
    width, height, quantities, shape_definitions, orientations_cache=None
):
    """Check if all required shapes can fit using DLX."""
    # Build list of shapes to place with unique IDs
    shapes_to_place = []
    for shape_idx, count in enumerate(quantities):
        for instance in range(count):
            shapes_to_place.append((shape_idx, instance))

    if not shapes_to_place:
        return True

    # Quick area check
    total_shape_area = sum(
        len(shape_to_coords(shape_definitions[shape_idx]))
        for shape_idx, _ in shapes_to_place
    )
    if total_shape_area > width * height:
        return False

    gap = width * height - total_shape_area

    # For large gaps (>100), greedy placement is sufficient and much faster
    if gap > 100:
        return can_fit_greedy(
            width, height, quantities, shape_definitions, orientations_cache
        )

    # Use cached orientations or compute them
    if orientations_cache:
        all_orientations = orientations_cache
    else:
        all_orientations = {}
        for shape_idx in set(idx for idx, _ in shapes_to_place):
            all_orientations[shape_idx] = get_all_orientations(
                shape_definitions[shape_idx]
            )

    # Create columns:
    # Primary: shape instances (must be used exactly once)
    # Secondary: grid cells (can be covered at most once - enforces non-overlap)
    primary_columns = []
    for shape_idx, instance in shapes_to_place:
        primary_columns.append(("shape", shape_idx, instance))

    secondary_columns = []
    for r in range(height):
        for c in range(width):
            secondary_columns.append(("cell", r, c))

    dlx = DLX(primary_columns, secondary_columns)

    # Add rows: each possible placement of each shape instance
    row_id = 0
    for shape_idx, instance in shapes_to_place:
        for orientation in all_orientations[shape_idx]:
            # Try each position
            for start_r in range(height):
                for start_c in range(width):
                    # Check if shape fits
                    cells_covered = []
                    valid = True
                    for dr, dc in orientation:
                        r, c = start_r + dr, start_c + dc
                        if r < 0 or r >= height or c < 0 or c >= width:
                            valid = False
                            break
                        cells_covered.append(("cell", r, c))

                    if valid:
                        # This row covers: cells used + this shape instance
                        row_columns = cells_covered + [("shape", shape_idx, instance)]
                        dlx.add_row(row_id, row_columns)
                        row_id += 1

    # Solve exact cover problem
    return dlx.search()


def solve(data):
    """Solve the puzzle."""
    shapes, regions = parse_input(data)

    # Pre-compute all orientations once for all regions
    all_orientations_cache = {}
    for shape_idx in shapes:
        all_orientations_cache[shape_idx] = get_all_orientations(shapes[shape_idx])

    count = 0
    for width, height, quantities in regions:
        if can_fit_region_dlx(
            width, height, quantities, shapes, all_orientations_cache
        ):
            count += 1

    return count


def solve_from_file(filename):
    """Read input from file and solve."""
    with open(filename, "r") as f:
        data = f.read()
    return solve(data)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
