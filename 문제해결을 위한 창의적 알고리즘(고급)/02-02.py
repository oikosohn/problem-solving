"""
숫자 뒤집기
- 재귀함수 
"""

import math

def solve(n: int):
    if n < 10:
        return n
    return solve(n//10) + (n%10) * pow(10, int(math.log10(n)))


m = int(input())

print(solve(m))