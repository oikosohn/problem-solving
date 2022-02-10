"""
삼각화단 만들기
- 전체탐색 시간 개선, O(n^2)
"""
def solve(n: int) -> int :
    cnt = 0
    for i in range(1, n+1): # 1<=a
        for j in range(i, n+1): # 1<=a<=b
            k = n - (i + j) # c == n - (i + j)
            if i+j > k and k >= j:
                cnt += 1
    return cnt

n = int(input())
print(solve(n))
