""""
1에서 n까지의 합
- 재귀함수, k == n/2
- O(logN)
"""

def f(n: int):
    if n == 1:
        return 1
    return 2*f(n//2) + ((n+1)//2) * ((n+1)//2)

num = int(input())

print(f(num))