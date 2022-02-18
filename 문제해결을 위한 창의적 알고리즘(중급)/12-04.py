"""
경찰차
- 경험적 배제 + 단순 탐욕법
    1. 두 경찰차가 하나의 사건을 처리하기 위해 필요한 거리 미리 계산
    2. 그 중 작은 값을 초기 min 값으로 설정
    3. 이동거리가 min보다 커지는 순간 탐색하지 않음
"""
def dis(a:int, b:int) -> int:
    return abs(e[a][0]-e[b][0]) + abs(e[a][1]-e[b][1])

def greedy(a: int, b: int):
    global ans

    for i in range(2, w+2):
        if dis(i, a) > dis(i, b):
            ans += dis(i, b)
            b = i
        else:
            ans += dis(i, a)
            a = i


n = int(input())
w = int(input())
e = [[0 for _ in range(2)] for _ in range(n+2)]
ans = 0

e[0][0] = e[0][1] = 1
e[1][0] = e[1][1] = n

for i in range(2, w+2):
    r, c = map(int, input().split())
    e[i][0], e[i][1] = r, c

greedy(0, 1)
print(ans)