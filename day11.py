from collections import defaultdict
if __name__ == '__main__':
    stones_count: defaultdict[int, int] = defaultdict(int)

    with open('input/day11.txt', 'r') as xs:
        for stone in map(int, xs.read().split()):
            stones_count[stone] += 1

    for blink in range(1, 75 + 1):
        curr_stones_count = stones_count.copy()
        for stone, curr_count in curr_stones_count.items():
            stones_count[stone] -= curr_count  # remove the stones we will transform
            ss, len_ss = str(stone), len(str(stone))
            if stone == 0:
                stones_count[1] += curr_count
            elif len_ss % 2 == 0:
                left, right = int(ss[:len_ss // 2]), int(ss[len_ss // 2:])
                stones_count[left] += curr_count
                stones_count[right] += curr_count
            else:
                stones_count[stone * 2024] += curr_count

        if blink == 25:  # part 1
            print(sum(stones_count.values()))

    print(sum(stones_count.values()))  # part 2
