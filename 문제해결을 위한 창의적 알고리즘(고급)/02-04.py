"""
별 그리기0
- 재귀함수 
"""

def solve(n: int):
    if n == 1:
        print('*')
    else:
        solve(n-1)
        print('*'*n)


m = int(input())

solve(m)