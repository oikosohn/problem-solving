"""
인접리스트로 구현하면 인접행렬보다 탐색 시간을 줄일 수 있다.
- 인접 행렬 : O(v*e)
- 인접 리스트 : O(v+e)
"""

from collections import deque

n, m = map(int, input().split())

adj = {i:[] for i in range(n)}

for i in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b,w)) # 양방향 그래프

print(adj)