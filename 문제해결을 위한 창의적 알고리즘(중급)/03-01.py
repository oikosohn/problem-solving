# 인접 행렬 구현

g = [[0 for _ in range(101)] for _ in range(101)]

n, m = map(int, input().split())
for i in range(m):
    a, b, w = map(int, input().split())
    g[a][b] = g[b][a] = w # 양방향 그래프

print(g)