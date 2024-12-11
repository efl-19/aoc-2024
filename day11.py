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
    blink_count = 25
    for i in range(blink_count):
        stones = blink(stones)

    print(len(stones))


