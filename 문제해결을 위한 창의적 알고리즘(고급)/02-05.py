"""
별 그리기2
- 재귀함수 
- O(n*n)
"""

def solve(n: int):
    if n == 1:
        print('*')
    else:
        solve(n-1)
        for i in range(n):
            print('*', end='')
        print()


m = int(input())

solve(m)