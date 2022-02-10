"""
최댓값, 데이터 입력받고 동시에 최댓값 찾기
"""

from typing import Union, List

def solve(matrix: list) -> Union[int, int, int]:
    n = 9
    ans, mi, mj = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if ans < matrix[i][j]:
                ans = matrix[i][j]
                mi = i+1
                mj = j+1
    return ans, mi, mj

grid: List[int] = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

v, x, y = solve(grid)
print(v)
print(x, y)