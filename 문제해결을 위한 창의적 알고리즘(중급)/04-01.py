"""
DFS / 두더지 굴 개수 및 굴의 크기 내림차순 출력
"""

def safe(a: int, b: int) -> bool:
    return (0<=a and a<n) and (0<=b and b<n)

def dfs(a, b, c): # (a,b) 에서 시작해서 모든 정점을 c로 바꾼다
    arr[a][b] = c
    if safe(a+1, b) and arr[a+1][b] == 1: # 하
        dfs(a+1, b, c)
    if safe(a-1, b) and arr[a-1][b] == 1: # 상
        dfs(a-1, b, c)
    if safe(a, b+1) and arr[a][b+1] == 1: # 우
        dfs(a, b+1, c)
    if safe(a, b-1) and arr[a][b-1] == 1: # 좌
        dfs(a, b-1, c)

n = int(input())
cnt = 0
size = list(0 for _ in range(101))
arr = []

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
