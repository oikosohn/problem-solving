"""
고기잡이(연못 2차원 확장)
- 전체탐색, O(n * m * w * h)
"""
def solve(n: int, w: int, value: list) -> int:
    ans = 0
    for i in range(n-h+1):
        for j in range(m-w+1):
            total_sum = 0
            for a in range(h):
                for b in range(w):
                    total_sum += value[i+a][j+b]
            if total_sum > ans:
                ans = total_sum
    return ans 

n, m = map(int, input().split()) # 연못 세로 길이, 가로 길이
h, w = map(int, input().split()) # 그물 세로 길이, 가로 길이

value = []
for _ in range(n):
    row = list(map(int, input().split()))
    value.append(row)

print(solve(n, w, value))