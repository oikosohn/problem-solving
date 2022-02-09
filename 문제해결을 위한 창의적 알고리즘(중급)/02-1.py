"""
lower bound : 찾고자 하는 값(k) 이상이 처음 나타나는 위치
"""

def solve(s: int, e: int) -> int:
    
    while e-s > 0:
        m = (s + e) // 2
        if arr[m] < k:
            s = m + 1
        else:
            e = m
    return e+1 # s >= e : e+1 반환


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(solve(0, n))