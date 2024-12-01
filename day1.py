from collections import Counter

if __name__ == '__main__':
    with open('input/day1.txt', 'r') as input_data:
        left, right = [], []
        for line in input_data.readlines():
            l, r = line.strip().split("   ")
            left.append(int(l))
            right.append(int(r))

    # part 1
    print(sum(abs(l - r) for l, r in zip(sorted(left), sorted(right))))

    # part 2
    count_right = Counter(right)
    print(sum(l * count_right[l] for l in left))
