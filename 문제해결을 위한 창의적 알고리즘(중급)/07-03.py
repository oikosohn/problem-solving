"""
리모컨, 최소횟수 구하기 문제 => BFS
- O(3n) 
"""
from collections import deque


a, b = map(int, input().split())

q = deque()
q.append((a, 0))

while q:
    temp, cnt = q.popleft()

    if temp == b:
        break

    if temp < b:
        q.append((temp+1, cnt+1))
        q.append((temp+5, cnt+1))
        q.append((temp+10, cnt+1))
    else:
        q.append((temp-1, cnt+1))
        q.append((temp-5, cnt+1))
        q.append((temp-10, cnt+1))

print(cnt)