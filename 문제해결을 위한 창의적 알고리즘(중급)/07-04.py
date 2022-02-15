"""
Minimum Sum, 재귀
- 
"""

def backtrack(row: int, score: int):
    global min_sum

    if row == n:
        if score < min_sum:
            min_sum = score
        return

    for i in range(n):
        if col_check[i] == 0:
            col_check[i] = 1 # col check
            # row+1: 줄바뀜 score+matrix[row][i]: 갱신된 값
            backtrack(row+1, score+matrix[row][i]) 
            col_check[i] = 0 # col check 해제 후 backtrack

    return

n = int(input())
matrix = []
min_sum = 10001
col_check = [0 for i in range(n)]

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

backtrack(0, 0)

print(min_sum)