"""
피보나치
- 상향식 동적표
"""

dt = [0 for _ in range(100001)]
n = int(input())

for i in range(1, n+1):
    if i == 1:
        dt[i] = 1
    else:
        dt[i] = i + dt[i-1]

print(dt[n])