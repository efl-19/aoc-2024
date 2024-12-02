from functools import reduce


def is_safe(level: list[int]) -> bool:
    return (
        (
            all(l1 > l2 for l1, l2 in zip(level, level[1:]))  # descending
            or all(l1 < l2 for l1, l2 in zip(level, level[1:]))  # ascending
        )
        and all(1 <= abs(l1 - l2) <= 3 for l1, l2 in zip(level, level[1:]))  # difference
    )


def is_safe_enough(level: list[int]) -> bool:
    return is_safe(level) or any(is_safe(level[:i] + level[i + 1:]) for i in range(len(level)))


def tuple_sum(t) -> tuple[int, int]:
    return reduce(lambda count, safe: (count[0] + safe[0], count[1] + safe[1]), t, (0, 0))


if __name__ == '__main__':
    with open('input/day2.txt', 'r') as xs:
        levels = ([int(l) for l in r.strip().split(" ")] for r in xs.readlines())

    print(tuple_sum(map(lambda level: (is_safe(level), is_safe_enough(level)), levels)))
