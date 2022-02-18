"""
경찰차
- 경험적 배제
"""
def dis(a:int, b:int) -> int:
    return abs(e[a][0]-e[b][0]) + abs(e[a][1]-e[b][1])

def solve(a:int, b:int, d:int):
    global ans

    next = max(a, b)+1

    # 현재까지 이동 거리 > 현재까지 최소 거리, 탐색 불필요
    if d > ans:
        return

    if next >= w+2:
        if d < ans:
            ans = d
        return

    solve(next, b, d+dis(a, next))
    solve(a, next, d+dis(b, next))


n = int(input())
w = int(input())
e = [[0 for _ in range(2)] for _ in range(n+2)]
ans = 987654321

e[0][0] = e[0][1] = 1
e[1][0] = e[1][1] = n

for i in range(2, w+2):
    r, c = map(int, input().split())
    e[i][0], e[i][1] = r, c

solve(0, 1, 0)
print(ans)