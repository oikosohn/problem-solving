"""
삼각화단 만들기
- 전체탐색 비선형 구조
"""

chk = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
n = int(input())
cnt = 0

def solve(n: int, a: int, b: int, c: int) -> int :
    global cnt
    if a+b+c == n:
        if a <= b <= c and a + b > c and chk[a][b][c] == 0:
            cnt += 1
            chk[a][b][c] = 1
        return
    solve(n, a+1, b, c)
    solve(n, a, b+1, c)
    solve(n, a, b, c+1)
    return cnt

print(solve(n, 1, 1, 1))