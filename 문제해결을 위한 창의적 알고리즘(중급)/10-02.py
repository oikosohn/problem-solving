"""
소방차, 재귀
"""

def solve(pt: int, ft: int, h: int):
    global mh

    if ft == f: # 모든 소방차에 펌프가 연결되면
        mh = min(mh, h)
        return
    
    for i in range(1, p+1): # i부터 펌프 개수까지 반복
        if pv[i] == 0:
            # 호스 선택
            pv[i] = 1
            h += abs(pp[i]-fp[ft+1]) 

            solve(i, ft+1, h)
            
            # 호스 미선택 (백트랙)
            h -= abs(pp[i]-fp[ft+1]) 
            pv[i] = 0


p, f = map(int, input().split())
pp = [0] + list(map(int, input().split()))
fp = [0] + list(map(int, input().split()))
pv = [0 for _ in range(p+1)]

mh = 987654321

solve(0, 0, 0)
print(mh)