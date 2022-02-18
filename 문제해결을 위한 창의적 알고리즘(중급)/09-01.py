""""
maximum sum, 구간 합 전체 탐색
- O(n^3)
"""

n = int(input())
a = list(map(int, input().split()))
ans = 0

for s in range(0, n):
    for e in range(s, n):
        total_sum = 0
        for k in range(s, e+1):
            total_sum += a[k]
        if ans < total_sum:
            ans = total_sum

print(ans)