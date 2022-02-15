"""
리모컨, 백트랙
- O(3^res)
"""
def backtrack(temp: int , cnt: int) :
    global res
    
    if cnt > res:
        return

    if temp == b:
        if cnt < res:
            res = cnt
        return

    if temp < b:
        backtrack(temp+1, cnt+1)
        backtrack(temp+5, cnt+1)
        backtrack(temp+10, cnt+1)
    else:
        backtrack(temp-1, cnt+1)
        backtrack(temp-5, cnt+1)
        backtrack(temp-10, cnt+1)

a, b = map(int, input().split())
res = 40

backtrack(a, 0)
print(res)