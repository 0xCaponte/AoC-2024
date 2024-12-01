#
#  Distance Between lists
#

import sys

list_1 = []
list_2 = []

for line in sys.stdin:

    x, y = line.split()
    list_1.append(int(x))
    list_2.append(int(y))

list_1.sort()
list_2.sort()

sum = 0

for element_1, element_2 in zip(list_1, list_2):
    sum += abs(element_1 - element_2)

print(sum)


