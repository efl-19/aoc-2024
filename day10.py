from collections import deque

class Grid:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.col_count = len(self.grid[0])
        self.row_count = len(self.grid)

    def _inbound(self, x: int, y: int):
        return 0 <= x < self.col_count and 0 <= y < self.row_count

    def _height(self, x: int, y: int) -> int:
        return int(self.grid[y][x]) if self.grid[y][x].isdigit() else -1

    def _neighbors(self, x: int, y: int):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return (
            (nx, ny)
            for dx, dy in directions
            if self._inbound((nx := x + dx), (ny := y + dy))  # TIL
        )

    def _starting_points(self) -> list[tuple[int, int]]:
        return [
            (i, j)
            for j in range(self.row_count)
            for i in range(self.col_count)
            if self.grid[j][i] == "0"
        ]

    def _trailhead_score(self, x: int, y: int) -> int:  # BFS for part 1
        visited = set()
        queue = deque([(x, y, 0)])
        reachable_nines = set()

        while queue:
            cx, cy, height = queue.popleft()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))

            if self.grid[cy][cx] == "9":
                reachable_nines.add((cx, cy))

            for nx, ny in self._neighbors(cx, cy):
                next_candidate_height = self._height(nx, ny)
                if next_candidate_height == height + 1:  # we can move
                    queue.append((nx, ny, next_candidate_height))

        return len(reachable_nines)

    def _trailhead_rating(self, x: int, y: int) -> int:  # DFS for part 2
        def dfs(cx: int, cy: int, height: int, visited: set[tuple[int, int]]) -> int:
            if (cx, cy) in visited or self._height(cx, cy) != height:
                return 0
            visited.add((cx, cy))

            total_trails = 1 if self.grid[cy][cx] == "9" else 0
            for nx, ny in self._neighbors(cx, cy):
                if self._height(nx, ny) == height + 1:
                    total_trails += dfs(nx, ny, height + 1, visited)
            visited.remove((cx, cy))
            return total_trails

        return dfs(x, y, 0, set())

    def total_trailhead_score(self) -> int:
        return sum(self._trailhead_score(x, y) for x, y in self._starting_points())

    def total_trailhead_rating(self) -> int:
        return sum(self._trailhead_rating(x, y) for x, y in self._starting_points())

    def pprint(self):
        for row in self.grid:
            print("".join(row))


if __name__ == '__main__':
    with open('input/day10.txt', 'r') as xs:
        grid = Grid([list(line.strip()) for line in xs.readlines()])

    print(grid.total_trailhead_score())
    print(grid.total_trailhead_rating())
