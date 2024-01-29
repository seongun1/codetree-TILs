import sys

max_val = -sys.maxsize

n,m,c = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
ans = []

def interact(a,b,c,d):
    return not (b < c or d < a)

def possible(x1,y1,x2,y2):
    if y1 + m - 1 >=n or y2 + m - 1 >=n :
        return False
    
    if x1 != x2:
        return True
    
    if interact(y1, y1+m-1,y2, y2+m-1):
        return False
    return True

def choose(idx, weight, val):
    global max_val

    if idx == m:
        if weight <= c:
            max_val = max(max_val, val)
        return
    
    choose(idx+1, weight, val)
    choose(idx+1, weight + ans[idx], val + ans[idx] ** 2)


def find_max(a,b):
    global ans, max_val

    ans = arr[a][b:b+m]
    max_val = 0
    choose(0,0,0)
    return max_val

for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                if possible(x1, y1, x2, y2):
                    max_val = max(max_val, find_max(x1, y1) + find_max(x2, y2))
print(max_val)