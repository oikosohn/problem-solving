""""
광석수집
- 반복 + 동적표 : O(n * m)
"""

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
board = [[0 for _ in range(210)] for _ in range(210)]
dt = [[0 for _ in range(210)] for _ in range(210)]

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, m+1):
        board[i][j] = row[j-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            dt[i][j] = board[i][j]
        else:
            dt[i][j] = max(dt[i-1][j], dt[i][j-1]) + board[i][j]

print(dt[n][m])