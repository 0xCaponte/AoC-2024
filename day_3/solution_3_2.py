

import sys
import re

dont_pattern = r"don't\(\).*?do\(\)"
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

text = sys.stdin.read() 
text = text + "do()" # Closes a possible final dont

# Remove segments betwent dont() and do()
matches = re.findall(dont_pattern, text, re.DOTALL) # DOTALL allows to match new lines

for match in matches:
    text = text.replace(match, '')

# Get valid multiplications
matches = re.findall(mul_pattern, text)

for match in matches:
    x,y = int(match[0]), int(match[1])
    total += x * y

print(total)
