"""
타일 채우기
- 재귀함수
- k = n-1 => f(k) = f(n-1)
- f(0) = 1
- f(1) = 1
- f(n) = f(n-1) + f(n-2) + f(n-2)
"""

def f(k: int):
    global m
    if k <= 1:
        return 1 % m
    else:
        return (f(k-1)+2*f(k-2)) % m

n = int(input())
m = int(input())

print(f(n))