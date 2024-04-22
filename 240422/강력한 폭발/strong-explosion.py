import sys

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

max_val = -sys.maxsize
boom = 0
ans = []
boomSite = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            boom += 1
            boomSite.append((i,j))

type_block = [
    [0],
    [(-2,0),(-1,0),(1,0),(2,0)],
    [(0,-1),(-1,0),(1,0),(0,1)],
    [(-1,-1),(-1,1),(1,-1),(1,1)]
]

def getSize():
    size = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                size += 1
    return size

def init_temp():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

def calc():
    init_temp()

    for i in ans:
        x,y,k = i

        temp[x][y] = 1

        for h in type_block[k]:
            nx,ny = x + h[0], y + h[1]

            if not in_range(nx,ny) or temp[nx][ny]:
                continue
            
            temp[nx][ny] = 1
    
    cnt =  getSize()
    return cnt
                

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def choose(cnt):
    global max_val

    if cnt == boom:
        max_val = max(max_val, calc())
        return
    
    for k in range(1,4):
        x,y = boomSite[cnt]

        ans.append((x,y,k))
        choose(cnt+1)
        ans.pop()

choose(0)
print(max_val)