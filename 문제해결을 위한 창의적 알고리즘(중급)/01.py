"""
강의 요약 : 데이터 정렬되어있으면 빠른 탐색을 위해 이분탐색 사용하자
"""

def solve(s: int, e: int) -> int:
    m = 0
    while e-s >= 0: # [s, e] 탐색
        m = (s+e) // 2 
        if arr[m] == k: # 중간 위치 계산
            return m+1 # 탐색 성공 시 위치 반환
        if arr[m] < k: # [s, e] 범위 수정
            s = m+1
        else:
            e = m-1
    return -1 # 값이 없는 경우 -1 반환


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(solve(0, n-1))