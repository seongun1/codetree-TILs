import sys

max_val = -sys.maxsize

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

boom = []
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            boom.append((i,j))

boom1 = [(-2,0),(-1,0),(1,0),(2,0)]
boom2 = [(-1,0),(0,-1),(1,0),(0,1)]
boom3 = [(-1,-1),(-1,1),(1,-1),(1,1)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def getSize():

    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for i in ans:
        num,x,y = i

        tmp[x][y] = 1

        if num == 1:
            for j in boom1:
                dx,dy = j

                next_x , next_y = x + dx, y + dy
                if not in_range(next_x, next_x):
                    continue
                 
                tmp[next_x][next_y] = 1
        elif num == 2:
            for j in boom2:
                dx,dy = j

                next_x , next_y = x + dx, y + dy
                if not in_range(next_x, next_x):
                    continue
                 
                tmp[next_x][next_y] = 1
        elif num == 3:
            for j in boom3:
                dx,dy = j

                next_x , next_y = x + dx, y + dy
                if not in_range(next_x, next_x):
                    continue
                 
                tmp[next_x][next_y] = 1
    size = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j]:
                size += 1
    return size

def choose(cnt):
    global max_val

    if cnt == len(boom):
        max_val = max(max_val , getSize())
        return
    
    for i in range(1,4):
        for j in boom:
            ans.append((i, j[0], j[1]))
            choose(cnt+1)
            ans.pop()

choose(0)
print(max_val)