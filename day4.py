class Grid:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.column_count = len(self.grid[0])
        self.row_count = len(self.grid)

    def _inbound(self, x: int, y: int):
        return 0 <= x < self.row_count and 0 <= y < self.column_count

    def _search_from(self, x: int, y: int, word: str, direction: tuple[int, int]):
        for i in range(len(word)):
            nx, ny = x + direction[0] * i, y + direction[1] * i
            if not self._inbound(nx, ny) or self.grid[nx][ny] != word[i]:
                return False
        return True

    def find_word_count(self, word: str) -> int:
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i in range(self.row_count):
            for j in range(self.column_count):
                if self.grid[i][j] == word[0]:
                    for direction in directions:
                        if self._search_from(i, j, word, direction):
                            count += 1
        return count


if __name__ == '__main__':
    with open('input/day4.txt', 'r') as xs:
        grid = Grid([list(line.strip()) for line in xs.readlines()])

    print(grid.find_word_count("XMAS"))
