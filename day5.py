from functools import cmp_to_key

ORDER_MAP: dict[int, list[int]] = {}


def custom_cmp(a: int, b: int) -> int:
    return -1 if b in ORDER_MAP[a] else 1


if __name__ == '__main__':
    with open('input/day5.txt', 'r') as xs:
        full_file = xs.read()
        a, b = full_file.split('\n\n')
        ordering_rules = [[int(e) for e in l.split('|')] for l in a.split('\n') if l]
        updates = [[int(e) for e in l.split(',')] for l in b.split('\n') if l]

    for a, b in ordering_rules:
        ORDER_MAP.setdefault(a, []).append(b)

    sum_middles_sorted, sum_middles_after_sort = 0, 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(custom_cmp))
        if update == sorted_update:  # part 1
            sum_middles_sorted += update[int((len(update) - 1) / 2)]
        else:  # part 2
            sum_middles_after_sort += sorted_update[int((len(sorted_update) - 1) / 2)]

    print(sum_middles_sorted, sum_middles_after_sort)
