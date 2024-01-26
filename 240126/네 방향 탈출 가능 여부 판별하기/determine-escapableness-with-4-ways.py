from collections import deque

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

x,y = 0,0
q = deque()
q.append((x,y))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] == 1 or arr[x][y] == 0:
        return False
    
    return True

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def bfs():

    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x,next_y = x + dx, y + dy

            if can_go(next_x, next_y):
                visited[next_x][next_y] = 1
                q.append((next_x,next_y))

bfs()

ans = visited[n-1][m-1]
print(ans)