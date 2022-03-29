"""
조합의 수
- 재귀함수
- else문 호출 횟수 2^k
"""

def solve(n: int, k: int):
    if k == n:
        return 1
    elif k == 1:
        return n
    else:
        # 마지막을 선택한 경우 + 마지막 선택하지 않은 경우
        return solve(n-1, k-1) + solve(n-1, k) 


a, b = map(int, input().split())

print(solve(a, b))