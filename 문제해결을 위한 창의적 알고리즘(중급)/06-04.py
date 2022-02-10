"""
고기잡이
- 전체탐색, O(n * w)
"""
def solve(n: int, w: int, value: list) -> int:
    ans = 0
    for i in range(n-w+1):
        total_sum = 0
        for j in range(w):
            total_sum += value[i+j]
        if total_sum > ans:
            ans = total_sum
    return ans 

n = int(input())
w = int(input())
value = list(map(int, input().split()))

print(solve(n, w, value))