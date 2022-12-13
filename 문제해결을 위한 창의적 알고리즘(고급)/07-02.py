""""
광석수집
- 재귀 + 동적테이블
"""
MOD = 1000000003

def f(a: int, b: int, can: bool):
    if b == k:
        return 1
    if a >= n-can:
        return 0

    if dt[can][a][b] == -1: 
        dt[can][a][b] = (f(a+1, b, can)+f(a+2, b+1, can)) % MOD

    return dt[can][a][b]

n = int(input())
k = int(input())

dt = [[[-1 for _ in range(2)] for _ in range(n+1)] for _ in range(k+1)]
print((f(1,0,0)+f(2,1,1)) % MOD)
# 1000000003
# c언어 최대 숫자 2^31-1 => 21억 