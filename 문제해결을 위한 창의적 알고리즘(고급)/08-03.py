"""
선물
- 동적테이블
- 전체탐색 : 3^20
- 모든 선물의 합 100 * 20 = 2000
"""

g = [0 for _ in range(21)] 
dt = [[[0 for _ in range(2)] for _ in range(668)] for _ in range(668)]
dt[0][0][0] = True

n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    g[i+1] = l[i]

w = sum(g)


for i in range(1, n+1):
    for a in range(668):
        for b in range(668):
            print(i, a, b)
            # 길동, 길순, 길삼 순으로 받음
            gildong = dt[(i-1)%2][a][b]

            if a < g[i]:
                gilsun = False
            else:
                gilsun = dt[(i-1)%2][a-g[i]][b]

            if b < g[i]:
                gilsam = False
            else:
                gilsam = dt[(i-1)%2][a][b-g[i]]

            # dt[i][a][b] = (dt[i-1][a][b]) or gilsun or gilsam


ans = 987654321
for a in range(668):
    for b in range(668):
        if dt[n%2][a][b]:
            if w-(a+b) >= a and a >= b and w-(a+b)-b <= ans:
                ans = w-(a+b)-b
                A = w-(a+b)
                B = a
                C = b

print(A, B, C)
