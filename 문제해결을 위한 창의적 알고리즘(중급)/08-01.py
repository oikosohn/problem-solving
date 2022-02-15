"""
치즈, flood fill기법
"""

def fill(x: int, y: int):
    if x < 1 or x > n or y < 1 or y > m:
        return
    if a1[x][y] == 0: # 공기라면
        a1[x][y] = 2 # 2로 체크

        # 연결된 0을 모두 2로 채움
        fill(x+1, y) 
        fill(x-1, y)
        fill(x, y+1)
        fill(x, y-1)

def check(x: int, y: int) -> int:
    t = 0
    # 인접한 공기 개수 체크
    if a1[x+1][y] == 2:
        t += 1
    if a1[x-1][y] == 2:
        t += 1
    if a1[x][y+1] == 2:
        t += 1
    if a1[x][y-1] == 2:
        t += 1
    return t

def copy():
    for i in range(1, n+1):
        for j in range(1, m+1):
            a1[i][j] = a2[i][j]

n, m = map(int, input().split())
a1 = [[0 for _ in range(m+1)] for _ in range(n+1)]
a2 = [[0 for _ in range(m+1)] for _ in range(n+1)]
hour = 0
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(1, n+1):
    for j in range(1, m+1):
        a1[i][j] = matrix[i-1][j-1]
        a2[i][j] = a1[i][j]

while(1):
    fill(1, 1) # 공기 2로 채움
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 치즈이면서 공기와 2면 접해있으면
            if a1[i][j] == 1 and check(i,j) >= 2:
                a2[i][j] = 0 # 녹음
                cnt += 1 # 시간 증가
    
    if cnt == 0: # 공기로 바뀐 것이 없음 => 다 녹았다
        print(hour) # 시간 출력
        break
    
    hour += 1
    copy() # a2 -> a1 복사