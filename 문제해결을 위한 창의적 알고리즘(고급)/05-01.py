"""
피보나치 
- 동적표
"""

dt = [0 for _ in range(100001)]


def f(n: int):
    if n <= 2:
        return 1
    if dt[n] == 0:
        dt[n] = f(n-1)+f(n-2)
    return dt[n]

m = int(input())
print(f(m))