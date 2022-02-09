"""
DFS / 두더지 굴 개수 및 굴의 크기 내림차순 출력
더 짧은  풀이
"""


def dfs(a, b, c): # (a,b) 에서 시작해서 모든 정점을 c로 바꾼다
    arr[a][b] = c
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            dfs(nx, ny, c)

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

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1 # 1, 2, 3
            dfs(i, j, cnt+1) # 2, 3, 4 

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            size[arr[i][j]-2] += 1
    
size = sorted(size[0:cnt])

print(cnt)
for i in range(cnt):
    print(size[i])
