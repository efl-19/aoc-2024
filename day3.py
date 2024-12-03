import re

if __name__ == '__main__':
    with open('input/day3.txt', 'r') as xs:
        lines = xs.readlines()

    s1, s2 = 0, 0
    p1, p2 = r'mul\((\d+),(\d+)\)', r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    enabled = True
    for line in lines:
        # part 1
        ms_1 = re.findall(p1, line)
        for a, b in ms_1:
            s1 += int(a) * int(b)

        # part 2
        ms_2 = re.findall(p2, line)
        for m in ms_2:
            if m == 'do()':
                enabled = True
            elif m == 'don\'t()':
                enabled = False
            else:  # mul(a, b)
                if enabled:
                    a, b = re.match(p1, m).groups()
                    s2 += int(a) * int(b)

    print(s1, s2)
