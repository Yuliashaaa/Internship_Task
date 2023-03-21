"""
Task 2. Counting islands
"""
import numpy as np

M = int(input('Enter M: '))
N = int(input('Enter N: '))
print('Enter Matrix (single line, separated by space): ')
elements = list(map(int, input().split()))
matrix = np.array(elements).reshape(M, N)

islands = 0
visited = set()

# Depth First Search (DFS) Algorithm
def DFS(i, j):
    visited.add((i, j))
    for m, n in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
        if (m in range(M)) and (n in range(N)) and ((m, n) not in visited) and (matrix[m][n] == 1):
            DFS(m, n)

# Couinting islands
for i in range(M):
    for j in range(N):
        if (matrix[i][j] == 1) and ((i, j) not in visited):
            islands += 1
            DFS(i, j)

print(islands)