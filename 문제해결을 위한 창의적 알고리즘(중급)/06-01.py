"""
삼각화단 만들기
- 전체탐색, O(n^3)
"""
def solve(n: int) -> int :
    cnt = 0
    for i in range(1, n+1): # 1<=a
        for j in range(i, n+1): # 1<=a<=b
            for k in range(j, n+1): # 1<=a<=b<=c
                if i+j+k == n and i+j > k:
                    cnt += 1
    return cnt

n = int(input())
print(solve(n))
