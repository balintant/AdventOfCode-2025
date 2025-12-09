#!/usr/bin/env python3
"""
Day 9: Movie Theater - Part 2
https://adventofcode.com/2025/day/9

Scanline algorithm to build polygon extent, then fast rectangle validation.
"""

import sys


def compute_polygon_extent(red_tiles):
    """
    For each y-coordinate, compute the x-range(s) where the polygon exists.
    Returns: dict mapping y -> list of (x_min, x_max) intervals, edges for point checking
    """
    n = len(red_tiles)

    # Get all unique y-coordinates in the polygon structure (vertices)
    polygon_ys = sorted(set(y for x, y in red_tiles))

    # Build edges for point-in-polygon checking
    edges = []
    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        edges.append(((x1, y1), (x2, y2)))

    # Build result map - only for y-coordinates that define the polygon structure
    y_to_x_ranges = {}

    # ONLY compute for polygon's structural y-coordinates, not all integers
    for y in polygon_ys:
        # Find all edge crossings at this y
        crossings = []

        for i in range(n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[(i + 1) % n]

            # Horizontal edge at this y
            if y1 == y2 == y:
                x_start, x_end = min(x1, x2), max(x1, x2)
                # Mark as horizontal edge
                crossings.append(("h", x_start, x_end))

            # Vertical edge crossing this y
            elif y1 != y2 and min(y1, y2) < y <= max(y1, y2):
                x_cross = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                crossings.append(("v", x_cross, x_cross))

        if not crossings:
            continue

        # Separate horizontal edges from vertical crossings
        h_edges = [(int(s), int(e)) for typ, s, e in crossings if typ == "h"]
        v_crosses = sorted([x for typ, x, _ in crossings if typ == "v"])

        # Build intervals from vertical crossings (interior fill)
        # For a closed polygon, vertical crossings must come in pairs
        if len(v_crosses) % 2 != 0:
            raise ValueError(
                f"Odd number of vertical crossings at y={y}: {len(v_crosses)}. "
                f"This indicates malformed polygon data."
            )

        intervals = []
        for idx in range(0, len(v_crosses) - 1, 2):
            x_start = int(v_crosses[idx])
            x_end = int(v_crosses[idx + 1])
            intervals.append((x_start, x_end))

        # Add horizontal edges
        intervals.extend(h_edges)

        # Merge overlapping intervals
        if intervals:
            intervals.sort()
            merged = [intervals[0]]
            for start, end in intervals[1:]:
                if start <= merged[-1][1] + 1:
                    merged[-1] = (merged[-1][0], max(merged[-1][1], end))
                else:
                    merged.append((start, end))

            y_to_x_ranges[y] = merged

    return y_to_x_ranges, edges


def is_interval_contained(intervals, x_min, x_max):
    """Check if [x_min, x_max] is fully contained in union of intervals."""
    for start, end in intervals:
        if start <= x_min and x_max <= end:
            return True
    return False


def point_in_polygon(x, y, edges):
    """Check if point is on boundary or inside polygon using ray casting."""
    # Check if on any edge
    for (x1, y1), (x2, y2) in edges:
        if y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2):
            return True
        if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2):
            return True

    # Ray casting for interior
    crossings = 0
    for (x1, y1), (x2, y2) in edges:
        if y1 == y2:
            continue
        if not (min(y1, y2) < y <= max(y1, y2)):
            continue
        x_cross = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        if x_cross > x:
            crossings += 1

    return crossings % 2 == 1


def solve(data):
    """Find the largest rectangle with red corners containing only red/green tiles."""
    # Parse red tiles
    red_tiles = []
    for line in data:
        line = line.strip()
        if line:
            x, y = map(int, line.split(","))
            red_tiles.append((x, y))

    if len(red_tiles) < 2:
        return 0

    # Build polygon extent map and get edges
    y_to_x_ranges, edges = compute_polygon_extent(red_tiles)

    # Get all polygon y-coordinates
    polygon_ys = set(y_to_x_ranges.keys())

    # Generate candidates sorted by area
    candidates = []
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)

            area = (x_max - x_min + 1) * (y_max - y_min + 1)
            candidates.append((area, x_min, x_max, y_min, y_max))

    candidates.sort(reverse=True)

    max_area = 0

    for area, x_min, x_max, y_min, y_max in candidates:
        if area <= max_area:
            break

        # Check corners first (quick rejection)
        corners = [(x_min, y_min), (x_max, y_min), (x_min, y_max), (x_max, y_max)]
        if not all(point_in_polygon(x, y, edges) for x, y in corners):
            continue

        # Check if rectangle is valid
        # Only check y-coordinates that are structural points of the polygon
        relevant_ys = [y for y in polygon_ys if y_min <= y <= y_max]

        valid = True
        for y in relevant_ys:
            x_ranges = y_to_x_ranges[y]
            if not is_interval_contained(x_ranges, x_min, x_max):
                valid = False
                break

        if valid:
            max_area = area
            break

    return max_area


def solve_from_file(filename):
    """Read input from file and solve the puzzle."""
    with open(filename, "r") as f:
        data = f.readlines()
    return solve(data)


def main():
    """Main entry point."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
