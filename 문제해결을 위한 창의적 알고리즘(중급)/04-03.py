"""
BFS 너비우선탐색
- 우선순위(예: 큐의 입력순서)에 따라 줄을 세워 방문
"""

from collections import deque

def bfs(a: int, b: int, c: int):
    q = deque()
    q.append((a, b))
    arr[a][b] = c

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if  0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = c
                q.append((nx, ny))

n = int(input())
cnt = 0
size = list(0 for _ in range(101))
arr = []

# 우하좌상
dx = (1, 0, -1, 0) 
dy = (0, 1, 0, -1)

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

print(arr)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1 # 1, 2, 3
            bfs(i, j, cnt+1) # 2, 3, 4 

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            size[arr[i][j]-2] += 1
    
size = sorted(size[0:cnt])

print(cnt)
for i in range(cnt):
    print(size[i])