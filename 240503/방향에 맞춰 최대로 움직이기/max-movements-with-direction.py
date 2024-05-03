import sys

n = int(input())
max_val = -sys.maxsize

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

direction_arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

x,y = map(int,input().split())
x -= 1
y -= 1

dxs = [0,-1,-1,0,1,1,1,0,-1]
dys = [0,0,1,1,1,0,-1,-1,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y, prev):
    return in_range(x,y) and arr[x][y] > prev

def choose(x,y, cnt):
    global max_val

    max_val = max(max_val, cnt)

    d = direction_arr[x][y]

    for i in range(n):
        nx,ny = x + dxs[d] * i, y + dys[d] * i
        if can_go(nx,ny,arr[x][y]):
            choose(nx,ny,cnt+1)

choose(x,y,0)
print(max_val)