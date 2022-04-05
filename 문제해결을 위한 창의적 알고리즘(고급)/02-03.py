"""
숫자 뒤집기
- 재귀함수 
"""

import math

def solve(n: int):
    if n < 10:
        return n
    t = pow(10, int(math.log10(n)))
    return (n%10) * t + solve((n%t)//10) * 10 + (n//t)


m = int(input())

print(solve(m))