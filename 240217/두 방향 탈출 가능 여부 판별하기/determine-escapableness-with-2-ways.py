n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

ans = [
    [0 for _ in range(m)]
    for _ in range(n)
]

res = 1
def dfs(x,y):
    global res

    dxs,dys = [1,0],[0,1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx , y + dy

        if can_go(nx,ny):
            ans[nx][ny] = 1
            visited[nx][ny] = 1
            dfs(nx,ny)

ans[0][0] = 1
visited[0][0] = True
dfs(0,0)

print(ans[n-1][n-1])