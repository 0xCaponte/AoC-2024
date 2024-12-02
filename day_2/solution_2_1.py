

import sys

safe_reports = 0

for line in sys.stdin:

    levels = list(map(int, line.split()))
    
    safe = True
    previous = None
    past_direction = None

    for level in levels:

        if previous is not None:

            # Direction
            ascending = level < previous

            if past_direction is None:
                past_direction = ascending
            
            if ascending != past_direction:
                safe = False
                break

            # Level difference
            diff = abs(level - previous)

            if  diff < 1 or diff > 3:
                safe = False
                break

        previous = level
    
    if safe:
        safe_reports += 1

print(safe_reports)

