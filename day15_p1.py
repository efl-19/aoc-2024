DIRECTIONS = {
    '^': (0, -1),
    'v': (0, 1),
    '>': (1, 0),
    '<': (-1, 0)
}


class Grid:
    def __init__(self, grid: list[list[str]]):
        self.col_count = len(grid[0])
        self.row_count = len(grid)
        self.robot = list(self._starting_points(grid, '@'))[0]
        self.boxes = self._starting_points(grid, 'O')
        self.walls = self._starting_points(grid, '#')

    def _starting_points(self, grid: list[list[str]], char: str) -> set[tuple[int, int]]:
        return {
            (i, j)
            for j in range(self.row_count)
            for i in range(self.col_count)
            if grid[j][i] == char
        }

    def _can_move(self, point: tuple[int, int], direction: tuple[int, int]) -> tuple[bool, tuple[int, int] | None]:
        cx, cy = point
        nx, ny = cx + direction[0], cy + direction[1]
        if not (nx, ny) in self.walls and not (nx, ny) in self.boxes:
            return True, (nx, ny)
        if (nx, ny) in self.walls:
            return False, None

        # nx, ny is a box
        return self._can_move((nx, ny), direction)

    def move(self, direction: tuple[int, int]):
        can_move, free_space = self._can_move(self.robot, direction)
        if can_move:
            self.robot = (self.robot[0] + direction[0], self.robot[1] + direction[1])
            if self.robot in self.boxes:
                self.boxes.remove(self.robot)
                self.boxes.add(free_space)

    def sum_boxes_coordinates(self) -> int:
        return sum(x + 100 * y for x, y in self.boxes)

    def pprint(self):
        for j in range(self.row_count):
            for i in range(self.col_count):
                if (i, j) == self.robot:
                    print('@', end='')
                elif (i, j) in self.boxes:
                    print('O', end='')
                elif (i, j) in self.walls:
                    print('#', end='')
                else:
                    print('.', end='')
            print()


if __name__ == '__main__':
    with open('input/day15_sample.txt', 'r') as xs:
        w_map, r_instructions = xs.read().split("\n\n")
        w_grid = Grid([list(line) for line in w_map.split("\n")])
        r_directions = [
            d
            for instructions in r_instructions.split("\n")
            for i in instructions
            if (d := DIRECTIONS.get(i))
        ]

    for direction in r_directions:
        w_grid.move(direction)

    w_grid.pprint()
    print(w_grid.sum_boxes_coordinates())
