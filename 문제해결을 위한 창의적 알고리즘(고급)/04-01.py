"""
이진 암호화
- 재귀함수, 인덱스와 길이 사용
- k : 시작하는 인덱스
- n : 문자열 길이
"""

def f(k: int, s: int):

    global password
    sum = 0

    if s == 1: # 더 이상 나뉠 수 없을 때
        print(password[k], end='')
        return

    # 모두 같다면 출력
    for i in range(k, k+s):
        sum += password[i]
    
    if (sum==0 or sum==s):
        print(int(bool(sum)), end='')
    else: #같지 않다면 분할
        print('-', end='')
        f(k, s//2)
        f(k+s//2, s//2)

n = int(input())
password = list(map(int, input()))
f(0, n)