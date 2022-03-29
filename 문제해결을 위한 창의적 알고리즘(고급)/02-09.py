"""
조합의 수
- 재귀함수
- 개선
"""

def solve(n: int, k: int):
    if k == n:
        return 1
    if k == 1:
        return n
    # 마지막을 선택한 경우 + 마지막 선택하지 않은 경우
    return solve(n, k-1) * (n-k+1) // k


a, b = map(int, input().split())

print(solve(a, b))