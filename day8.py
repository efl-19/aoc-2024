import itertools

if __name__ == '__main__':
    with open('input/day8.txt', 'r') as xs:
        grid = [list(line.strip()) for line in xs.readlines()]

    row_count = len(grid[0])
    column_count = len(grid)
    grid_map = {}
    for i in range(row_count):
        for j in range(column_count):
            frequency = grid[j][i]
            if frequency.isalnum():
                grid_map.setdefault(frequency, []).append((i, j))

    antinodes_p1: set[tuple[int, int]] = set()
    antinodes_p2: set[tuple[int, int]] = set()

    for antennas in grid_map.values():
        for (x1, y1), (x2, y2) in list(itertools.combinations(antennas, 2)):
            dx, dy = x2 - x1, y2 - y1  # distance

            # part 1
            a1_x, a1_y = x1 - dx, y1 - dy
            a2_x, a2_y = x2 + dx, y2 + dy
            if 0 <= a1_x < row_count and 0 <= a1_y < column_count and (a1_x, a1_y) not in antennas:
                antinodes_p1.add((a1_x, a1_y))

            if 0 <= a2_x < row_count and 0 <= a2_y < column_count and (a2_x, a2_y) not in antennas:
                antinodes_p1.add((a2_x, a2_y))

            # part 2
            current_x, current_y = x1, y1
            while 0 <= current_x < row_count and 0 <= current_y < column_count:
                antinodes_p2.add((current_x, current_y))
                current_x, current_y = current_x - dx, current_y - dy

            current_x, current_y = x1, y1
            while 0 <= current_x < row_count and 0 <= current_y < column_count:
                antinodes_p2.add((current_x, current_y))
                current_x, current_y = current_x + dx, current_y + dy

    print(len(antinodes_p1))
    print(len(antinodes_p2))
