import sys

n,m = map(int,input().split())

min_val = sys.maxsize

arr = [
    tuple(map(int,input().split()))
    for _ in range(m)
]
ans = list()

def getDist(a,b):
    x1, y1 = a
    x2, y2 = b
    return (x2-x1) ** 2 + (y2-y1) ** 2

def choose(idx, cnt):
    global min_val

    if cnt == m:
        max_val = -sys.maxsize
        for i, val in enumerate(ans):
            for j, val1 in enumerate(ans):
                if i < j:
                    max_val = max(max_val, getDist(val, val1))
        min_val = min(min_val, max_val)

    if idx == n:
        return
    
    ans.append(arr[idx])
    choose(idx+1, cnt + 1)
    ans.pop()
    choose(idx+1, cnt)
choose(0,0)
print(min_val)