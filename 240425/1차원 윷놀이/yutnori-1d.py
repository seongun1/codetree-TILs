import sys

n,m,k = map(int,input().split())
move = list(map(int,input().split()))

ans = [1] * k
max_val = -sys.maxsize

def calc():
    cnt = 0
    for i in ans:
        if i >= m:
            cnt += 1
    return cnt

def choose(cnt):
    global max_val

    if cnt == n:
        max_val = max(max_val, calc())
        return
    
    for i in range(k):
        ans[i] += move[cnt]
        choose(cnt+1)
        ans[i] -= move[cnt]

choose(0)
print(max_val)