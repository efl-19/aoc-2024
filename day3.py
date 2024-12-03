import re

if __name__ == '__main__':
    s1, s2 = 0, 0
    enabled = True
    with open('input/day3.txt', 'r') as xs:
        for line in xs.readlines():
            ms = re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
            for m in ms:
                if m == 'do()':
                    enabled = True
                elif m == 'don\'t()':
                    enabled = False
                else:  # mul(a, b)
                    a, b = map(int, re.match('mul\((\d+),(\d+)\)', m).groups())
                    s1 += a * b
                    if enabled:
                        s2 += a * b

    print(s1, s2)
