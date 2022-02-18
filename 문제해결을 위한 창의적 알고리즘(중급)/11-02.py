"""
소수들의 합, 수학적 배제
"""

n = int(input())
ans = 0

def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True

for i in range(2, n+1):
    if is_prime(i):
        ans += i

print(ans)
