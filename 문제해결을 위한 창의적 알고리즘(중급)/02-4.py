"""
upper bound : 찾고자 하는 값보다 큰 값이 처음으로 나타나는 위치

bisect 활용
"""
import bisect

def solve() -> int:
    answer = bisect.bisect_right(arr, k) + 1
    return answer

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(solve())