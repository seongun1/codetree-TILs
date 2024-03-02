from collections import deque
import sys

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

time, size = 0,0 # 녹는데 걸린시간, 마지막 빙하 크기

dxs, dys = [-1,1,0,0],[0,0,-1,1]

q = deque()
glaciers_to_melt = deque()

def has_ice():
    for row in arr:
        for elem in row:
            if elem: # 빙하라면
                return True
    
    return False

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and not arr[x][y]

def is_ice(x, y):
    return in_range(x, y) and not visited[x][y] and arr[x][y]

def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def bfs():
    init_visited()
    
    q.append((0,0))
    visited[0][0] = True

    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True

def outside_water(x,y):
    for dx, dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy

        if in_range(nx,ny) and visited[nx][ny]: # 빙하로 둘러싸여 있지 않음
            return True
    return False

def melt():
    global size

    for i in range(n):
        for j in range(m):
            if arr[i][j] and outside_water(i,j):
                arr[i][j] = 0
                size += 1

def simulate():
    global size, time

    time += 1
    size = 0

    bfs()
    melt()

while True:
    simulate()

    if not has_ice():
        break

print(time, size)