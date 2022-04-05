"""
노드 간 거리
- 재귀 함수
- 특징
  1. 두 노드 간 경로 오직 한 개
  2. 완전 이진 트리 배열 저장
    - c의 부모노드 index : c//2
    - c의 왼쪽 자식 노드 index : c * 2
    - c의 오른쪽 자식 노드 index : c * 2 + 1
  3. 노드의 번호가 클수록 루트와 거리가 멀다.
- f(a, b) = 0 ,a=b
- f(a, b) = f(a//2, b) + 1, a > b
- f(a, b) = f(a, b//2) + 1, a < b
"""

def f(a: int, b: int):
    if a == b:
        return 0
    if b > a :
        return f(a, b//2) + 1
    if a > b:
        return f(a//2 , b) + 1

n, m = map(int, input().split())

print(f(n, m))