""""
거스름 돈

730
5
10 50 100 500 1250
- 엄청 오래 걸림
"""

# 깊이 우선 탐색과 유사
def solve(mon: int, d: int):
    global ans

    # 추가 배제 조건 필요 -> 12-01.py

    if mon > m:
        return

    if mon == m:
        if d < ans:
            ans = d
        return

    for i in range(n):
        solve(mon+coin[i], d+1)

m = int(input())
n = int(input())
coin = list(map(int, input().split()))
ans = 987654321

solve(0, 0)
print(ans)