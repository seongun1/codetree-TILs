import sys

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

max_val = -sys.maxsize
ans = [1] * k

def calc():
    cnt = 0
    for i in ans:
        if i >= m:
            cnt += 1
    return cnt

def choose(idx):
    global max_val

    if idx == n:
        max_val = max(max_val, calc())
        return

    for i in range(k):
        if ans[i] >= m:
            continue
        
        ans[i] += arr[idx]
        choose(idx+1)
        ans[i] -= arr[idx]

    return

choose(0)
print(max_val)