import math
import re
from collections import Counter
from dataclasses import dataclass


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]

    @staticmethod
    def parse(line: str) -> "Robot":
        (x, y), (vx, vy) = re.findall(r'[a-z]=(-?\d+),(-?\d+)', line)
        return Robot((int(x), int(y)), (int(vx), int(vy)))


class Grid:
    def __init__(self, robots: list[Robot], row_count: int, col_count: int):
        self.robots = robots
        self.row_count = row_count
        self.col_count = col_count

    def move(self, seconds: int = 1):
        for robot in self.robots:
            x, y = robot.position
            vx, vy = robot.velocity
            robot.position = ((x + vx * seconds) % self.col_count, (y + vy * seconds) % self.row_count)

    def safety_factor(self) -> int:
        center_row = self.row_count // 2
        center_col = self.col_count // 2
        q1, q2, q3, q4 = 0, 0, 0, 0
        for (x, y) in (robot.position for robot in self.robots):
            if x == center_col or y == center_row:
                continue
            if x > center_col and y < center_row:
                q1 += 1
            elif x < center_col and y < center_row:
                q2 += 1
            elif x < center_col and y > center_row:
                q3 += 1
            elif x > center_col and y > center_row:
                q4 += 1

        return q1 * q2 * q3 * q4

    def pprint(self):
        grid = [['.' for _ in range(self.col_count)] for _ in range(self.row_count)]
        count_pos = Counter((x, y) for x, y in (robot.position for robot in self.robots))
        for (x, y), count in count_pos.items():
            grid[y][x] = str(count)
        for row in grid:
            print(''.join(row))


if __name__ == '__main__':
    with open('input/day14.txt', 'r') as xs:
        robots = [Robot.parse(line) for line in xs.readlines()]

    grid = Grid(robots, row_count=103, col_count=101)
    grid.move(seconds=100)
    print(grid.safety_factor())  # part 1

    min_safety_factor = math.inf
    min_safety_factor_second = 0
    for second in range(101, 10000):
        grid.move(seconds=1)
        sf = grid.safety_factor()
        if sf < min_safety_factor:
            min_safety_factor = sf
            min_safety_factor_second = second
            grid.pprint()

    print(min_safety_factor_second)  # part 2
