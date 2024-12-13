import math
import re
from dataclasses import dataclass, astuple


@dataclass(frozen=True)
class Instruction:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]

    @staticmethod
    def parse(instruction: str) -> "Instruction":
        a, b, prize = instruction.split("\n")[:3]
        return Instruction(
            a=tuple(map(int, re.findall(r'[XY][+=](\d+)', a))),
            b=tuple(map(int, re.findall(r'[XY][+=](\d+)', b))),
            prize=tuple(map(int, re.findall(r'[XY][+=](\d+)', prize)))
        )


if __name__ == '__main__':
    with open('input/day13.txt', 'r') as xs:
        instructions = map(Instruction.parse, xs.read().split("\n\n"))

    tokens_spent = 0
    for (ax, ay), (bx, by), (px, py) in map(astuple, instructions):
        min_cost = math.inf
        for a_press in range(0, 100 + 1):
            for b_press in range(0, 100 + 1):
                if ax * a_press + bx * b_press == px and ay * a_press + by * b_press == py:
                    min_cost = min(min_cost, 3 * a_press + b_press)
        if min_cost != math.inf:
            tokens_spent += min_cost

    print(tokens_spent)


