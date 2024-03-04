import sys

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

max_val = 0
ans = [1] * k

def calc():
    global max_val
    cnt = 0
    for i in ans:
        if i >= m:
            cnt += 1
    max_val = max(max_val, cnt)

def choose(idx):
    global max_val

    if idx == n:
        calc()
        return

    for i in range(k):
        if ans[i] >= m:
            continue
        
        ans[i] += arr[idx]
        choose(idx+1)
        ans[i] -= arr[idx]

    calc()
    return

choose(0)
print(max_val)