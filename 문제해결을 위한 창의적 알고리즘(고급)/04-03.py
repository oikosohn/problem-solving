"""
이진 복원
- 재귀함수, 큐
k : index
n : 원문 문자열 길이
v : 0 or 1
"""
from collections import deque

def f(k: int, s: int, v: str):
    global q, answer

    if len(q) == 0: # 모두 복원되었다면
        return
    
    if v == '-': # 분할되었다
        q.popleft()
        f(k, s//2, q[0]) # q[0] 다음 v
        q.popleft()
        f(k+2//2, s//2, q[0])
    else: # 영역 내 동일한 값을 가짐
        for _ in range(k, k+s):
            answer.append(v)

n = int(input())
password = list(map(str, input()))
q = deque(password)
answer = []

f(0, n, password[0])
for i in answer:
    print(i, end='')




