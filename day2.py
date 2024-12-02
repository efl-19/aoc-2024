def is_safe(level: list[int]) -> bool:
    return (
        (
            all(l1 > l2 for l1, l2 in zip(level, level[1:]))  # descending
            or all(l1 < l2 for l1, l2 in zip(level, level[1:]))  # ascending
        )
        and all(1 <= abs(l1 - l2) <= 3 for l1, l2 in zip(level, level[1:]))  # difference
    )


if __name__ == '__main__':
    with open('input/day2.txt', 'r') as input_data:
        levels = (
            [int(l) for l in report.strip().split(" ")]
            for report in input_data.readlines()
        )

    safe_count_p1 = 0
    safe_count_p2 = 0
    for level in levels:
        if is_safe(level):
            safe_count_p1 += 1
            safe_count_p2 += 1
        else:
            # brute force all level combinations
            if any(is_safe(level[:i] + level[i+1:]) for i in range(len(level))):
                safe_count_p2 += 1

    print(safe_count_p1)
    print(safe_count_p2)
