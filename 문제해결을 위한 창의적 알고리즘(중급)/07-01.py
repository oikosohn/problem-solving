"""
리모컨, 재귀
- O(6^res)
"""

def recur(temp: int , cnt: int) :
    global res
    
    if cnt > res:
        return

    if temp == b:
        if cnt < res:
            res = cnt
        return

    recur(temp+1, cnt+1)
    recur(temp+5, cnt+1)
    recur(temp+10, cnt+1)
    recur(temp-1, cnt+1)
    recur(temp-5, cnt+1)
    recur(temp-10, cnt+1)

a, b = map(int, input().split())
res = 40

recur(a, 0)
print(res)