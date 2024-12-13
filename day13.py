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


def brute_force(instructions: list[Instruction]) -> int:  # part 1
    tokens_spent = 0
    for (ax, ay), (bx, by), (px, py) in map(astuple, instructions):
        min_cost = math.inf
        for a_press in range(0, 100 + 1):
            for b_press in range(0, 100 + 1):
                if ax * a_press + bx * b_press == px and ay * a_press + by * b_press == py:
                    min_cost = min(min_cost, 3 * a_press + b_press)
        if min_cost != math.inf:
            tokens_spent += min_cost
    return tokens_spent


def optimized(instructions: list[Instruction]) -> int:  # part 2
    # Wizard maths I copied.. apparently called Cramer's rule (https://en.wikipedia.org/wiki/Cramer%27s_rule)
    tokens_spent = 0
    for (ax, ay), (bx, by), (px, py) in map(astuple, instructions):
        px += 10000000000000
        py += 10000000000000
        a_press = (px * by - bx * py) / (ax * by - bx * ay)
        b_press = (px * ay - ax * py) / (bx * ay - ax * by)

        if a_press == int(a_press) and b_press == int(b_press):
            tokens_spent += int(a_press * 3 + b_press)

    return tokens_spent

if __name__ == '__main__':
    with open('input/day13.txt', 'r') as xs:
        instructions = list(map(Instruction.parse, xs.read().split("\n\n")))

    print(brute_force(instructions))  # part 1
    print(optimized(instructions))  # part 2
