"""
약수의 합, 수학적 배제
- 최대 입력 : 100억
"""


n = int(input())
ans = 0

for i in range(1, n+1):
    if i*i < n and n % i == 0:
        ans += i + n//i

    if i*i == n: # 완전 제곱수이면 i를 더한다
        ans += i

print(ans)
