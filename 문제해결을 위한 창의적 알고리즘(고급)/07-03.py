""""
광석수집
- 점화식 = f(n, k)
  1. 첫 번째나 두 번째 색 중 한 가지 색을 이미 고른 경우 = f(n-2, k-1)
  2. 첫 번째 색, 두 번째 색 모두 고르지 않은 경우 = f(n-1, k)
  3. k > n/2 => 0, k=1 => n
"""
MOD = 1000000003

n = int(input())
k = int(input())

dt = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(2, n+1):
    for j in range(1, n//2+1):
        if j == 1:
            dt[i][j] = i
        else:
            dt[i][j] = (dt[i-2][j-1] + dt[i-1][j]) % MOD

print(dt[n][k])
