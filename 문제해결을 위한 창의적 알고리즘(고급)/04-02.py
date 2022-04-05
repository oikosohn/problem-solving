"""
이진 암호화
- 재귀함수, 인덱스만 사용
- a : password[a]
- b : password[b]
"""

def f(s: int, e: int):
    global password
    
    for i in range(s, e):
        # 같은 문자열로 구성되어 있는지 확인
        if password[i] == password[i+1]:
            continue
        else:
            print('-', end='')
            # 문자열이 같지 않으면 분할
            f(s, (s+e)//2)
            f((s+e)//2+1, e)
            return
    
    print(password[e], end='')

n = int(input())
password = list(map(int, input()))

f(0, n-1)