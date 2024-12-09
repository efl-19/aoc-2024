from itertools import chain


def find_all_indices(blocks: list[str], predicate: callable) -> list[int]:
    return [i for i, char in enumerate(blocks) if predicate(char)]

def find_last_index(l: list[list[str]], element: list[str]) -> int:
    for index in range(len(l) - 1, -1, -1):
        if l[index] == element:
            return index
    raise ValueError("Element not found in list")

def checksum_p1(blocks: list[str]) -> int:
    final_blocks = blocks.copy()
    free_space_indices = find_all_indices(final_blocks, lambda x: x == '.')
    digits_indices = find_all_indices(final_blocks, lambda x: x.isdigit())
    for fs_i, d_i in zip(free_space_indices, reversed(digits_indices)):
        if fs_i >= d_i:  # no more swaps needed
            break
        final_blocks[fs_i], final_blocks[d_i] = final_blocks[d_i], final_blocks[fs_i]  # swap

    c_sum = 0
    for i, id in enumerate(final_blocks):
        if not id.isdigit():
            break
        c_sum += int(id) * i
    return c_sum


def checksum_p2(blocks: list[list[str]]) -> int:
    final_blocks = blocks.copy()

    for block in reversed(blocks):
        if block[0].isdigit():
            for fi, f_block in enumerate(final_blocks):
                if f_block[0] == '.' and len(f_block) >= len(block):  # possible swap
                    li = find_last_index(final_blocks, block)
                    if fi >= li:  # no more swaps needed
                        break
                    if len(f_block) == len(block):  # simple swap
                        final_blocks[fi], final_blocks[li] = final_blocks[li], final_blocks[fi]
                    else:  # complex swap
                        final_blocks[fi], final_blocks[li] = final_blocks[li], len(block) * ['.']
                        remaining_dots = (len(f_block) - len(block)) * ['.']
                        final_blocks.insert(fi + 1, remaining_dots)
                    break

    c_sum = 0
    for i, id in enumerate(chain.from_iterable(final_blocks)):
        if not id.isdigit():
            continue
        c_sum += int(id) * i
    return c_sum


if __name__ == '__main__':
    with open('input/day9.txt', 'r') as xs:
        digits = list(map(int, xs.read().strip()))

    # part 1
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

    print(checksum_p1(blocks))

    # part 2
    id = 0
    blocks = []
    for i, digit in enumerate(digits):
        if i % 2 == 0:  # length of a file
            blocks.append([str(id)] * digit)
            id += 1
        elif digit != 0:  # free space
            blocks.append(["."] * digit)

    print(checksum_p2(blocks))
