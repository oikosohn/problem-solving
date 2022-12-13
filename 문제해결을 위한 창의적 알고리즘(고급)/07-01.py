""""
광석수집
- 재귀
"""
MOD = 1000000003

def f(a: int, b: int, can: bool):
    if b == k:
        return 1
    if a >= n-can:
        return 0
    return (f(a+1, b, can)+f(a+2, b+1, can)) % 1000000003

n = int(input())
k = int(input())

print((f(1,0,0)+f(2,1,1)) % MOD)

# 1000000003
# c언어 최대 숫자 2^31-1 => 21억 