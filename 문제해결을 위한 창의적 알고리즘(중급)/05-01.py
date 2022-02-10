"""
약수의 합 구하기 1
"""
from re import I


def sovle(n: int) -> int:
    ans = 0
    for i in range(1, n+1):
        if n % i == 0: # n이 i로 나누어지면
            ans += i   # 합에 더함
    return ans

n = int(input())
print(sovle(n))