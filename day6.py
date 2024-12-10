from copy import deepcopy


class Grid:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.visited_grid = deepcopy(grid)
        self.col_count = len(self.grid[0])
        self.row_count = len(self.grid)

    def _inbound(self, x: int, y: int):
        return 0 <= x < self.col_count and 0 <= y < self.row_count

    def _neighbor(self, x: int, y: int, dx: int, dy: int) -> str | None:
        nx, ny = x + dx, y + dy
        return self.grid[ny][nx] if self._inbound(nx, ny) else None

    def _starting_point(self) -> tuple[int, int]:
        for i in range(self.col_count):
            for j in range(self.row_count):
                if self.grid[j][i] == "^":
                    return i, j
        raise ValueError("No starting point found")

    def count_guard_path(self) -> int:
        ci, cj = self._starting_point()
        visited: set[tuple[int, int]] = set()
        visited_with_direction: set[tuple[int, int, int, int]] = set()

        self.visited_grid[cj][ci] = "X"
        dx, dy = 0, -1  # up
        visited.add((ci, cj))
        visited_with_direction.add((ci, cj, dx, dy))
        while self._inbound(ci, cj):
            nn = self._neighbor(ci, cj, dx, dy)
            if not nn:  # out of bound
                break
            if nn == "#":
                dx, dy = -dy, dx  # turn direction 90 degree right
            else:  # we can move
                ci, cj = ci + dx, cj + dy
                if self._inbound(ci, cj):
                    if (ci, cj, dx, dy) in visited_with_direction:  # loop
                        return 0
                    visited.add((ci, cj))
                    visited_with_direction.add((ci, cj, dx, dy))
                    self.visited_grid[cj][ci] = "X"

        return len(visited)

    def brute_force_loop_count(self):
        loop_count = 0
        for i in range(self.col_count):
            for j in range(self.row_count):
                if self.grid[j][i] == ".":
                    self.grid[j][i] = "#"
                    if self.count_guard_path() == 0:
                        loop_count += 1
                    self.grid[j][i] = "."
        return loop_count

    def pprint(self):
        for row in self.visited_grid:
            print("".join(row))


if __name__ == '__main__':
    with open('input/day6.txt', 'r') as xs:
        grid = Grid([list(line.strip()) for line in xs.readlines()])

    print(grid.count_guard_path())
    print(grid.brute_force_loop_count())  # this is a bit slow.. but it works eventually
