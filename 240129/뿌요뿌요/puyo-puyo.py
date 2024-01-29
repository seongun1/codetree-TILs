import sys

n = int(input())
boom = 0
max_val = -sys.maxsize

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,val):

    if not in_range(x,y):
        return False

    if visited[x][y] == True or arr[x][y] != val:
        return False

    return True

def dfs(x,y):
    global tmp, max_val

    for dx, dy in zip(dxs, dys):
        
        next_x , next_y = x + dx, y + dy

        if can_go(next_x, next_y, arr[x][y]):
            tmp += 1
            visited[next_x][next_y] = True
            dfs(next_x, next_y)
        
    max_val = max(max_val, tmp)

for i in range(n):
    for j in range(n):
        if can_go(i,j, arr[i][j]):
            tmp = 1
            visited[i][j] = True
            dfs(i,j)
            if tmp >= 4:
                boom += 1
print(boom, max_val)