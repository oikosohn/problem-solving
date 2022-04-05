"""
이진 복원
- 재귀함수, 배열
k : index
n : 원문 문자열 길이
v : 0 or 1
"""
def f(k: int, s: int):
    global p, answer
    
    v = password[p]
    p += 1

    if v == None: # 모두 복원되었다면
        return
    
    if v == '-': # 분할되었다
        f(k, s//2,) # q[0] 다음 v
        f(k+2//2, s//2)
    else: # 영역 내 동일한 값을 가짐
        for _ in range(k, k+s):
            answer.append(v)

n = int(input())
p = 0

password = list(map(str, input()))
answer = []

f(0, n)

for i in answer:
    print(i, end='')
