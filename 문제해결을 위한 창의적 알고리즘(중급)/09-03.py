""""
거스름 돈, 상태 트리 깊이 최소화(백트래킹)
"""

# 넓이 우선 탐색과 유사
# k번 이하의 동전을 cnt개 사용해 mon원을 거슬러줌
def solve(mon:int, k:int, cnt:int):
    global ans

    if k == n or mon > m:
        return
        
    if mon == m:
        if cnt < ans:
            ans = cnt
        return
    
    for i in range(m):
        if mon+coin[k]*i <= m:
            solve(mon+coin[k]*i, k+1, cnt+i)

m = int(input())
n = int(input())
coin = list(map(int, input().split()))
ans = 987654321

solve(0, 0, 0)
print(ans)