def find_word_count_in_grid(grid: list[str], word: str) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def search(x: int, y: int):
        c = 0
        for dx, dy in directions:
            valid = True
            for i in range(1, len(word)):
                nx, ny = x + dx * i, y + dy * i
                if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                    valid = False
                    break
            if valid:
                c += 1
        return c

    match_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                match_count += search(i, j)

    return match_count


word = "XMAS"

if __name__ == '__main__':
    with open('input/day4.txt', 'r') as xs:
        grid = [line.strip() for line in xs.readlines()]

    print(find_word_count_in_grid(grid, word))
