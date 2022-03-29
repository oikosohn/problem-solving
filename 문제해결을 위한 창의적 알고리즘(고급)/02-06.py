"""
별 그리기3
- 재귀함수
- O(n)
"""

def solve(n: int):
    if n > 0:
        solve(n-1)
        star[n] = '*'
        print(''.join(filter(None, star)))


m = int(input())
star = [None for _ in range(m+1)]

solve(m)