from collections import deque

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

x,y = 0,0
q = deque()
q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x , next_y = x + dx ,y + dy

            if can_go(next_x, next_y):
                visited[next_x][next_y] = visited[x][y] + 1
                q.append((next_x,next_y))

bfs()
if visited[n-1][m-1] == 0 or arr[n-1][m-1] == 0:
    print(-1)
else:
    print(visited[n-1][m-1])