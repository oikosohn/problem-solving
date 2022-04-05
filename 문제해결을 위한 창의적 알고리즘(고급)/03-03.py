"""
타일 채우기
- 재귀함수 + 피보나치 수열
- f(n) = f(n-1) + f(n-2) + f(n-2)
"""

n = int(input())
m = int(input())
arr = [1, 1]

for i in range(2, n+1):
    arr.append((arr[i-1] % m + 2 * arr[i-2] % m) % m)

print(arr[n])