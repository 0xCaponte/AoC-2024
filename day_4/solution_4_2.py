import sys

word = "MAS"
matrix = []
total_rows = 0
total_cols = 0

def check_x_words(matrix, y, x):

     # Check valid neighbors in both diagonals
    if (0 <= y - 1 < total_rows and 0 <= x - 1 < total_cols and 
        0 <= y + 1 < total_rows and 0 <= x + 1 < total_cols and
        0 <= y - 1 < total_rows and 0 <= x + 1 < total_cols and 
        0 <= y + 1 < total_rows and 0 <= x - 1 < total_cols):
        
        # top-left to bottom-right
        diagonal1 = matrix[y-1][x-1] + matrix[y][x] + matrix[y+1][x+1]
       
        # top-right to bottom-left
        diagonal2 = matrix[y+1][x-1] + matrix[y][x] + matrix[y-1][x+1]
        
        # Check if either diagonal is "MAS" or "SAM"
        if ((diagonal1 == word or diagonal1 == word[::-1]) 
            and (diagonal2 == word or diagonal2 == word[::-1])):

            return True
        
    return False
            

#################

for line in sys.stdin:
    row = list(line.strip())
    matrix.append(row)

# Valid bounds
total_rows = len(matrix)
total_cols = len(matrix[0])

total = 0

# Traverse matrix - Avoid start on the edges
for y in range(1, len(matrix) - 1):
    for x in range(1, len(matrix[y]) - 1): 
        
        # Search starting at the center of the target word - "A"
        if matrix[y][x] == 'A': 
           
           if check_x_words(matrix, y, x):
                total += 1

print(total)
