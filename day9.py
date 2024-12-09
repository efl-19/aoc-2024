from itertools import chain


def find_all_indices(blocks: list[str], predicate: callable) -> list[int]:
    return [i for i, char in enumerate(blocks) if predicate(char)]


def find_last_index(l: list[list[str]], element: list[str]) -> int:
    for index in range(len(l) - 1, -1, -1):
        if l[index] == element:
            return index
    raise ValueError("Element not found in list")


def checksum(blocks: list) -> int:
    return sum(int(id) * i if id.isdigit() else 0 for i, id in enumerate(blocks))


def part1(digits: list[int]) -> int:
    # build blocks
    id = 0
    blocks = []
    for i, digit in enumerate(digits):
        if i % 2 == 0:  # length of a file
            for _ in range(digit):
                blocks.append(str(id))
            id += 1
        else:  # free space
            for _ in range(digit):
                blocks.append(".")

    # transform to final blocks position
    final_blocks = blocks.copy()
    free_space_indices = find_all_indices(final_blocks, lambda x: x == '.')
    digits_indices = find_all_indices(final_blocks, lambda x: x.isdigit())
    for free_space_i, digit_i in zip(free_space_indices, reversed(digits_indices)):
        if free_space_i >= digit_i:  # no more swaps needed
            break
        final_blocks[free_space_i], final_blocks[digit_i] = final_blocks[digit_i], final_blocks[free_space_i]  # swap

    return checksum(final_blocks)


def part2(digits: list[int]) -> int:
    # build blocks
    id = 0
    blocks = []
    for i, digit in enumerate(digits):
        if i % 2 == 0:  # length of a file
            blocks.append([str(id)] * digit)
            id += 1
        elif digit != 0:  # free space
            blocks.append(["."] * digit)

    # transform to final blocks position
    final_blocks = blocks.copy()
    for right_block in reversed(blocks):
        if right_block[0].isdigit():
            for left_i, left_block in enumerate(final_blocks):
                if left_block[0] == '.' and len(left_block) >= len(right_block):  # possible swap detected
                    right_i = find_last_index(final_blocks, right_block)
                    if left_i >= right_i:  # no more swaps needed
                        break
                    if len(left_block) == len(right_block):  # simple swap
                        final_blocks[left_i], final_blocks[right_i] = final_blocks[right_i], final_blocks[left_i]
                    else:  # complex swap with remaining free space
                        final_blocks[left_i], final_blocks[right_i] = final_blocks[right_i], len(right_block) * ['.']
                        remaining_dots = (len(left_block) - len(right_block)) * ['.']
                        final_blocks.insert(left_i + 1, remaining_dots)
                    break

    final_blocks = list(chain.from_iterable(final_blocks))
    return checksum(final_blocks)


if __name__ == '__main__':
    with open('input/day9.txt', 'r') as xs:
        digits = list(map(int, xs.read().strip()))

    print(part1(digits))
    print(part2(digits))
