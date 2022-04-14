""""
광석수집
- 재귀 + 동적표 : O(n * m)
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

def solve(a:int, b:int):
    if dt[a][b] == 0:
        if a==n and b==m:
            dt[a][b] = board[a][b]
        elif a > n or b > m:
            dt[a][b] = 0
        else:
            dt[a][b] = max( solve(a+1, b), solve(a, b+1) ) + board[a][b]
    
    return dt[a][b]

print(solve(1, 1))