from itertools import product
from operator import add, mul
from typing import Callable


def solve(equations: list[tuple[int, tuple[int]]], operators: tuple[Callable]) -> int:
    matches: set[int] = set()
    for t, ns in equations:
        for p in product(operators, repeat=len(ns) - 1):
            result = ns[0]
            for i, n in enumerate(ns[1:]):
                result = p[i](result, n)
            if result == t:  # found a combination that equals to t
                matches.add(t)
                break

    return sum(matches)


if __name__ == '__main__':
    equations = []
    with open('input/day7.txt', 'r') as xs:
        for l in xs.readlines():
            t, ns = l.split(":")
            equations.append((int(t), tuple(map(int, ns.strip().split(" ")))))

    print(solve(equations, (add, mul)))  # part 1
    print(solve(equations, (add, mul, lambda a, b: int(str(a) + str(b)))))  # part 2
