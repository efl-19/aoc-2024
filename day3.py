import re

if __name__ == '__main__':
    s1, s2, enabled = 0, 0, True
    with open('input/day3.txt', 'r') as xs:
        for line in xs.readlines():
            for m in re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line):
                if m in {'do()', 'don\'t()'}:  # flip the switch
                    enabled = m == 'do()'
                else:  # mul(a, b)
                    a, b = map(int, re.match('mul\((\d+),(\d+)\)', m).groups())
                    s1 += a * b
                    if enabled:
                        s2 += a * b

    print(s1, s2)
