def matches(candidate: str, word):
    return candidate == word or candidate[::-1] == word


class Grid:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.column_count = len(self.grid[0])
        self.row_count = len(self.grid)

    def _inbound(self, x: int, y: int):
        return 0 <= x < self.row_count and 0 <= y < self.column_count

    def _neighbor(self, x: int, y: int, dx: int, dy: int) -> str | None:
        nx, ny = x + dx, y + dy
        return self.grid[nx][ny] if self._inbound(nx, ny) else None

    def _search_word(self, x: int, y: int, word: str, dx: int, dy: int) -> bool:
        for i, char in enumerate(word):
            nx, ny = x + dx * i, y + dy * i
            if not self._inbound(nx, ny) or self.grid[nx][ny] != char:
                return False
        return True

    def find_xmas_count(self) -> int:
        word = "XMAS"
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i in range(self.row_count):
            for j in range(self.column_count):
                if self.grid[i][j] == word[0]:
                    for dx, dy in directions:
                        if self._search_word(i, j, word, dx, dy):
                            count += 1
        return count

    def find_x_mas_count(self):
        word = "MAS"
        count = 0
        for i in range(self.row_count):
            for j in range(self.column_count):
                if self.grid[i][j] == word[1]:
                    top_left = self._neighbor(i, j, -1, -1)
                    bottom_right = self._neighbor(i, j, 1, 1)
                    top_right = self._neighbor(i, j, -1, 1)
                    bottom_left = self._neighbor(i, j, 1, -1)
                    if top_left and bottom_right and top_right and bottom_left:
                        x1 = top_left + word[1] + bottom_right
                        x2 = top_right + word[1] + bottom_left
                        if matches(x1, word) and matches(x2, word):
                            count += 1

        return count


if __name__ == '__main__':
    with open('input/day4.txt', 'r') as xs:
        grid = Grid([list(line.strip()) for line in xs.readlines()])

    print(grid.find_xmas_count())
    print(grid.find_x_mas_count())
