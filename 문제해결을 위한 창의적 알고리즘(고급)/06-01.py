""""
광석수집
- 위아래만 이동
- 깊이 우선 탐색 : 2^(n+m-1)
"""
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
board = [[0 for _ in range(m+1)] for _ in range(n+2)]

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, m+1):
        board[i][j] = row[j-1]

def solve(a:int, b:int):
    # 종료 조건
    if a == n and b == m:
        return board[n][m]
    
    # 경계 조건
    if a > n or b > m : 
        return 0

    # 탐색
    return max(solve(a+1, b), solve(a, b+1)) + board[a][b]

print(solve(1, 1))