"""
진법 변환2
- 재귀함수
"""

def f(n: int, k: int):
    if n > 0 :
        f(n//k , k)    
        print(d[n%k])

d = '0123456789ABCDEFGHIJ'
n, k = map(int, input().split())
f(n,k)