

import sys
from collections import deque

word = "XMAS"
matrix = []
total_rows = 0
total_cols = 0
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Up-left
    (-1, 1),  # Up-right
    (1, -1),  # Down-left
    (1, 1)    # Down-right
]

unique_paths = set()


def dfs_word_search(matrix, start_row, start_col):
    
    visited = set()
    queue = []

    # Explore in a specific direction
    for dy, dx in directions:

        queue.append((start_row, start_col, [(start_row, start_col)], dy, dx))
        visited.add((start_row, start_col))

        while queue:
            row, col, path, dir_y, dir_x = queue.pop(0)

            # Get explored word
            path_word = ''.join(matrix[r][c] for r, c in path)

            # Sub-Word doesnt match anymore, path not relevant
            if not (word.startswith(path_word) or word.startswith(path_word[::-1])):
                continue

            # Forms the word (forwards or backwards)
            if path_word == word or path_word == word[::-1]:            
                path = tuple(sorted(path)) # Backward and Forward Paths are the same
                unique_paths.add(path)
                break

            new_row, new_col = row + dir_y, col + dir_x

            if ((0 <= new_row < total_rows) 
                and (0 <= new_col < total_cols) 
                and ((new_row, new_col) not in visited)):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, path + [(new_row, new_col)], dir_y, dir_x))

    return unique_paths

#################

for line in sys.stdin:
    row = list(line.strip())
    matrix.append(row)

# Square-Matrix Sizes
total_rows = len(matrix)
total_cols = len(matrix[0])

# Traverse matrix          
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        
        # Check only if we can start or finish the word
        if matrix[y][x] == word[0] or matrix[y][x] == word[-1]: 
           dfs_word_search(matrix, y, x)

print(len(unique_paths))
