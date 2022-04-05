"""
타일 채우기
- 재귀함수
- k = n/2 => f(k) = f(n//2)
- n 짝수 = - n 홀수 = f(k//2) * f(k//2) + 2 * f(k//2-1) * f(k//2-1)
- n 홀수 = f(k//2) * f(k//2+1) + 2 * f(k//2) * f(k//2-1)
- f(0) = 1
- f(1) = 1
"""

def f(k: int):
    global m
    if k <= 1:
        return 1 % m
    if k % 2 :
        return (f(k//2) * f(k//2+1) + 2 * f(k//2) * f(k//2-1)) % m
    return (f(k//2) * f(k//2) + 2 * f(k//2-1) * f(k//2-1)) % m

n = int(input())
m = int(input())

print(f(n))