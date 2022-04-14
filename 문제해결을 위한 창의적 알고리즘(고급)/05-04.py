"""
피보나치
- 하향식 동적표
"""

dt = [0 for _ in range(100001)]

def f(n: int):
    if dt[n] == 0:
        if n == 1:
            dt[n] = 1
        else:
            dt[n] = f(n-1) + n
    return dt[n]

m = int(input())
print(f(m))