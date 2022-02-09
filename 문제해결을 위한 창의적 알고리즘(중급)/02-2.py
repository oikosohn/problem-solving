"""
lower bound : 찾고자 하는 값(k) 이상이 처음 나타나는 위치

bisect 활용
"""
import bisect

def solve() -> int:
    answer = bisect.bisect_left(arr, k) + 1
    return answer

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(solve())