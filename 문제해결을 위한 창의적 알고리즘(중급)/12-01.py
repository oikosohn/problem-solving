"""
거스름돈
- 배제 조건만 적용
"""

def solve(mon: int, d: int):
    global ans

    # 배제조건 : 현재까지 사용한 동전 개수 > 지금까지 구한 동전 개수
    if d > ans: 
        return

    # 현재 동전 합계가 거슬러줄 돈보다 크다면
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