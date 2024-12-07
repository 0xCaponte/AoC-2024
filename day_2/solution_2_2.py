

import sys


def test_with_dampener(levels):

    basic_test_safe, _ = test_levels(levels)

    if basic_test_safe:
        return True

    # Brute-Force removing each element
    for i in range(len(levels)):
        
        modified_levels = levels[:i] + levels[i+1:]
        safe_dampener_test, _ = test_levels(modified_levels)

        if safe_dampener_test:
            return True

    return False


def test_levels(levels):
   
    safe = True
    previous = None
    past_direction = None

    for i, level in enumerate(levels):

        if previous is not None:
        
            # Direction
            ascending = level < previous

            if past_direction is None:
                past_direction = ascending

            if ascending != past_direction:
                safe = False
                return safe, i

            # Level difference
            diff = abs(level - previous)

            if not 1 <= diff <= 3:
                safe = False
                return safe, i

        previous = level

    return safe, -1  # Return -1 if no failure occurred


safe_reports = 0

for line in sys.stdin:

    levels = list(map(int, line.split()))
    safe = test_with_dampener(levels)

    if safe:
        safe_reports += 1

print(safe_reports)

