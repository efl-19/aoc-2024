def find_all_indices(blocks: list[str], predicate: callable) -> list[int]:
    return [i for i, char in enumerate(blocks) if predicate(char)]


def checksum(blocks: str) -> int:
    final_blocks = list(blocks)
    free_space_indices = find_all_indices(final_blocks, lambda x: x == '.')
    digits_indices = find_all_indices(final_blocks, lambda x: x.isdigit())
    for fs_i, d_i in zip(free_space_indices, reversed(digits_indices)):
        if fs_i >= d_i:  # no more swaps needed
            break
        print(fs_i, d_i)
        final_blocks[fs_i], final_blocks[d_i] = final_blocks[d_i], final_blocks[fs_i]  # swap

    c_sum = 0
    for i, id in enumerate(final_blocks):
        if not id.isdigit():
            break
        c_sum += int(id) * i
    return c_sum


if __name__ == '__main__':
    with open('input/day9.txt', 'r') as xs:
        digits = list(map(int, xs.read().strip()))

    print(digits)

    id = 0
    blocks = ""
    for i, digit in enumerate(digits):
        if i % 2 == 0:  # length of a file
            blocks += str(id) * digit
            id += 1
        else:  # free space
            blocks += "." * digit
    print(blocks)
    print(checksum(blocks))
