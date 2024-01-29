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

    tmp =[[0] * n for _ in range(n)]

    for i in ans:
        num,x,y = i

        tmp[x][y] = 1

        if num == 1:
            for j in boom1:
                next_x, next_y = j

                if not in_range(x + next_x, y + next_y):
                    continue

                tmp[x + next_x][y + next_y] = 1

        elif num == 2:
            for j in boom2:
                next_x, next_y = j

                if not in_range(x + next_x, y + next_y):
                    continue

                tmp[x + next_x][y + next_y] = 1

        elif num == 3:
            for j in boom3:
                next_x, next_y = j

                if not in_range(x + next_x, y + next_y):
                    continue

                tmp[x + next_x][y + next_y] = 1
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
        x,y = boom[cnt]

        ans.append((i, x,y))
        choose(cnt+1)
        ans.pop()

choose(0)
print(max_val)