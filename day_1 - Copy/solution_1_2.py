#
#  Similarity Score
#

import sys

scores = {} # Dict of tuples -> number = (times in l1, times in l2)

for line in sys.stdin:

    x, y = line.split()
    x = int(x)
    y = int(y)

    # Check element from 1st list
    if x not in scores:
        # 1st time the number is seen        
        scores[x] = [1, 0]

    else:
        
        if scores[x][1] < 0:
            # had already appeared in the 2nd list
            scores[x] = [1,  abs(scores[x][1])]
        else:
            scores[x][0] += 1
        
    # Check element from 2nd list
    if y in scores:

        if scores[y][1] < 0:
            # still not found in the 1st list
            scores[y] = [0, abs(scores[y][1])]

        scores[y][1] += 1

    else:
        # 1st time it appears is in the 2nd list
        scores[y] = [0,-1]

sum = 0
for key, value in scores.items():

    times_in_1, times_in_2 = value

    if times_in_1 <= 0 or times_in_2 <= 0:
        continue;
    
    else:
        sum += key * times_in_1 * times_in_2

print(sum)