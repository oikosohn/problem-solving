"""
두 색 칠하기, DFS
"""

from collections import defaultdict

def dfs(v: int, c: int):
    visited[v] = c
    can = 1
    for i in range(n):
        # v에 연결되어있고 색이 같다면
        if matrix[v][i] and visited[i] == c:
            can = 0

    if not can: # 방문 불가
        visited[v] = 0 # 방문한 곳 체크 해제
        return # 백트랙

    for i in range(n):
        # 방문하지 않았고 연결된 모든 경우에 대해서
        if not visited[i] and matrix[v][i]:
            dfs(i, 1) # 빨강(1) 칠하기
            dfs(i, 2) # 검정(2) 칠하기

n = int(input())
m = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]
# g = defaultdict(list)
# g = {i: [] for i in range(n)}

for _ in range(m):
    s, e = map(int, input().split())
    matrix[s][e] = matrix[e][s] = 1
    # g[s].append(e)

dfs(0, 1)

ans = True
for i in range(n):
    if visited[i] == 0:
        ans = False

if ans :
    print('OK')
else:
    print('IMPOSSIBLE')