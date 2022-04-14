"""
피보나치
- 상향식 동적표 + 메모리 절약
"""

dt = 0
n = int(input())

for i in range(1, n+1):
    # dt[i] == dt[i-1] + i
    dt = dt + i

print(dt)