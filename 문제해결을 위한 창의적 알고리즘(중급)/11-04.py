"""
삼각화단 만들기
"""

n = int(input())
cnt = 0

for c in range(n//3, n//2+1):
    for a in range(1, n//3+1):
        b = n-(a+c)
        if a+b > c and (a <= b and b <= c):
            cnt += 1

print(cnt)
    
    