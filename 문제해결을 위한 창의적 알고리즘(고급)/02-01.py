"""
숫자 뒤집기
- 재귀함수 
"""

def solve(n: int):
    if n == 0:
        return
    if n%10:
        print(n%10)
    solve(n//10)


m = int(input())

solve(m)