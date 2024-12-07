

import sys
import re


mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

for line in sys.stdin:

    matches = re.findall(mul_pattern, line)

    for match in matches:
        x,y = int(match[0]), int(match[1])
        total += x * y

    print(total)
