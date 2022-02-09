"""
upper bound : 찾고자 하는 값보다 큰 값이 처음으로 나타나는 위치
"""

def solve(s: int, e: int) -> int:
    
    while e-s > 0: # e == s면 종료
        m = (s + e) // 2
        if arr[m] <= k: # arr[m] == k일 때도 포함
            s = m + 1
        else:
            e = m
    return e+1 # s >= e : e+1 반환


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(solve(0, n))