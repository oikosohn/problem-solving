"""
최댓값, 데이터 입력과 동시에 최대값 찾기
"""

ans = 0
mi, mj = 0, 0
for i in range(9):
    row = list(map(int, input().split()))
    if ans < max(row):
        ans = max(row)
        mi, mj = i+1, row.index(ans)+1

print(ans)
print(mi, mj)