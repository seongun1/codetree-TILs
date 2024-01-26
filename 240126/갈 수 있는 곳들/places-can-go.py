from collections import deque

n,k = map(int,input().split())

dxs,dys = [-1,1,0,0],[0,0,-1,1]

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

q = deque()
for i in range(k):
    x,y = tuple(map(int,input().split()))
    visited[x-1][y-1] = 1
    q.append((x-1,y-1))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 1 or arr[x][y]:
        return False
    return True

def bfs():
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x ,next_y = x + dx, y + dy

            if can_go(next_x, next_y):
                visited[next_x][next_y] = 1
                q.append((next_x, next_y))


bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1
print(cnt)