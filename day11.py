def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        str_stone = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(str_stone) % 2 == 0:
            left, right = str_stone[:len(str_stone) // 2], str_stone[len(str_stone) // 2:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(stone * 2024)

    return new_stones


if __name__ == '__main__':
    with open('input/day11.txt', 'r') as xs:
        stones = list(map(int, xs.read().split()))

    stones_count: dict[int, int] = {}
    for stone in stones:
        stones_count[stone] = stones_count.get(stone, 0) + 1

    for i in range(1, 75 + 1):
        previous_stones_count = stones_count.copy()
        for stone, curr_count in previous_stones_count.items():
            stones_count[stone] = stones_count.get(stone, 0) - curr_count
            str_stone = str(stone)
            if stone == 0:
                stones_count[1] = stones_count.get(1, 0) + curr_count
            elif len(str_stone) % 2 == 0:
                left, right = str_stone[:len(str_stone) // 2], str_stone[len(str_stone) // 2:]
                stones_count[int(left)] = stones_count.get(int(left), 0) + curr_count
                stones_count[int(right)] = stones_count.get(int(right), 0) + curr_count
            else:
                stones_count[stone * 2024] = stones_count.get(stone * 2024, 0) + curr_count

        if i == 25:  # part 1
            print(sum(stones_count.values()))

    print(sum(stones_count.values()))  # part 2








