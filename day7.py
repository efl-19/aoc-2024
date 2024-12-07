from itertools import product
from operator import add, mul
from typing import Callable, Iterable


def solve(equations: tuple[tuple[int, tuple[int, ...]], ...], operators: Iterable[Callable]) -> int:
    matches: set[int] = set()
    for test_result, numbers in equations:
        for fn in product(operators, repeat=len(numbers) - 1):
            result = numbers[0]
            for i, n in enumerate(numbers[1:]):
                result = fn[i](result, n)
            if result == test_result:  # found a combination that equals to t
                matches.add(test_result)
                break

    return sum(matches)


if __name__ == '__main__':
    with open('input/day7.txt', 'r') as xs:
        eqs = tuple(
            (int(t), tuple(map(int, ns.strip().split(" "))))
            for t, ns in (l.split(":") for l in xs.readlines())
        )

    print(solve(eqs, (add, mul)))  # part 1
    print(solve(eqs, (add, mul, lambda a, b: int(str(a) + str(b)))))  # part 2
