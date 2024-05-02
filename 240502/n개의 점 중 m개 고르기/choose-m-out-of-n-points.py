import sys
n,m = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

min_val = sys.maxsize

ans = []

def getDist(a,b):
    x1,y1 = a
    x2,y2 = b
    return (x2-x1) ** 2 + (y2-y1) ** 2

def choose(idx, cnt):
    global min_val

    if cnt == m:
        max_val = -sys.maxsize
        for i, val1 in enumerate(ans):
            for j, val2 in enumerate(ans):
                if i != j:
                    max_val = max(max_val, getDist(val1, val2))
        min_val = min(min_val, max_val)
        return
    
    if idx == n:
        return
    
    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)