from collections import deque

n,k,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y]:
        return False
    return True

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs(x, y):
    q = deque()
    q.append((x, y))

    init_visited()
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    
    return cnt

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def find_stone():
    stones = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                stones.append((i,j))
    return stones

def del_stone(start, stones, cnt, idx):
    global ans
    if cnt >= m:
        for x, y in start:
            ans = max(ans, bfs(x, y))
        return

    if idx >= len(stones):
        return

    for stone in stones:
        x, y = stone
        if arr[x][y] == 1:
            arr[x][y] -= 1
            del_stone(start, stones, cnt+1, idx+1)
            arr[x][y] += 1

start = []
for i in range(k):
    x,y = map(int,input().split())
    start.append((x-1,y-1))

ans = 0
def move():
    global start

    stones = find_stone()

    del_stone(start, stones, 0, 0)
    
    print(ans)
move()