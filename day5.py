from functools import cmp_to_key

ORDER_MAP: dict[int, list[int]] = {}


def custom_cmp(a: int, b: int) -> int:
    if not ORDER_MAP.get(a):
        return 1

    if b in ORDER_MAP[a]:
        return -1

    cmp = any(custom_cmp(bigger_than_a, b) for bigger_than_a in ORDER_MAP[a])
    return 1 if cmp else -1


if __name__ == '__main__':
    with open('input/day5.txt', 'r') as xs:
        full_file = xs.read()
        a, b = full_file.split('\n\n')
        ordering_rules = [[int(e) for e in l.split('|')] for l in a.split('\n') if l]
        updates = [[int(e) for e in l.split(',')] for l in b.split('\n') if l]

    for a, b in ordering_rules:
        ORDER_MAP.setdefault(a, []).append(b)

    sum_middles_sorted, sum_middle_after_sort = 0, 0
    for updates in updates:
        sorted_updates = sorted(updates, key=cmp_to_key(custom_cmp))
        if updates == sorted_updates:
            sum_middles_sorted += updates[int((len(updates) - 1)/2)]
        else:
            sum_middle_after_sort += sorted_updates[int((len(sorted_updates) - 1)/2)]

    print(sum_middles_sorted, sum_middle_after_sort)
