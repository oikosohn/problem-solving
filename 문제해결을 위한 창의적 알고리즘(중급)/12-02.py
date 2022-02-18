"""
거스름돈
- 배제 조건 + 단순 탐욕법
"""

def greedy(mon: int):
    global ans
    while mon:
        for i in range(n-1, -1, -1): # 가장 큰 동전부터 지불
            ans += mon // coin[i]
            mon %= coin[i]

m = int(input())
n = int(input())
coin = list(map(int, input().split()))
ans = 0

greedy(m)
print(ans)