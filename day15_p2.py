DIRECTIONS = {
    '^': (0, -1),
    'v': (0, 1),
    '>': (1, 0),
    '<': (-1, 0)
}


class Grid:
    def __init__(self, grid: list[str]):
        wide_grid = []
        for row in grid:
            new_row = row.replace('O', '[]').replace('.', '..').replace('#', '##').replace('@', '@.')
            wide_grid.append(list(new_row))
        self.col_count = len(wide_grid[0])
        self.row_count = len(wide_grid)
        self.robot = list(self._starting_points(wide_grid, '@'))[0]
        self.boxes = {tuple([(x, y), (x + 1, y)]) for (x, y) in self._starting_points(wide_grid, '[')}
        self.walls = self._starting_points(wide_grid, '#')

    def _starting_points(self, grid: list[list[str]], char: str) -> set[tuple[int, int]]:
        return {
            (i, j)
            for j in range(self.row_count)
            for i in range(self.col_count)
            if grid[j][i] == char
        }

    @property
    def _left_boxes(self) -> set[tuple[int, int]]:
        return {left for left, _ in self.boxes}

    @property
    def _right_boxes(self) -> set[tuple[int, int]]:
        return {right for _, right in self.boxes}

    def _can_move(self, point: tuple[int, int], direction: tuple[int, int]) -> tuple[bool, tuple[int, int] | None]:
        # TBD
        pass

    def move(self, direction: tuple[int, int]):
        # TBD
        pass

    def sum_boxes_coordinates(self) -> int:
        return sum(x + 100 * y for x, y in self.boxes)

    def pprint(self):
        for j in range(self.row_count):
            for i in range(self.col_count):
                if (i, j) == self.robot:
                    print('@', end='')
                elif (i, j) in self.walls:
                    print('#', end='')
                else:
                    placed = False
                    if (i, j) in self._left_boxes:
                        print('[', end='')
                        placed = True
                    elif (i, j) in self._right_boxes:
                        print(']', end='')
                        placed = True
                    if not placed:
                        print('.', end='')
            print()


if __name__ == '__main__':
    with open('input/day15_sample.txt', 'r') as xs:
        w_map, r_instructions = xs.read().split("\n\n")
        w_grid = Grid([line for line in w_map.split("\n")])
        r_directions = [
            d
            for instructions in r_instructions.split("\n")
            for i in instructions
            if (d := DIRECTIONS.get(i))
        ]

    w_grid.pprint()
