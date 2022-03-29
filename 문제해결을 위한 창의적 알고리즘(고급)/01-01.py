""""
1에서 n까지의 합
- 재귀함수, k == n-1
- log(N)
"""

def f(n: int):
    if n == 1:
        return 1
    return f(n-1) + n

num = int(input())

print(f(num))