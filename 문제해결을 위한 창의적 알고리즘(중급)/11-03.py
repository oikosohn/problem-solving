"""
n번째 소수 구하기, 수학적 배제
"""

n = int(input())
ans = 0

def prime_list(k):

    a = [False, False] + [True] * 100000
    primes = []

    for i in range(2, len(a)):
        if a[i]:
            primes.append(i)
            for j in range(i+i, len(a), i):
                a[j] = False

    return primes[n-1]

ans = prime_list(n)

print(ans)