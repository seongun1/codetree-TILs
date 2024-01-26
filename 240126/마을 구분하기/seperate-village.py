n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited =[
    [False for _ in range(n)]
    for _ in range(n)
]

cnt = 0
ans = list()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or arr[x][y] == 0:
        return False
    
    return True

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y):
    global cnt

    for dx, dy in zip(dxs, dys):
        next_x ,next_y = x + dx, y + dy

        if can_go(next_x, next_y):
            visited[next_x][next_y] = True
            cnt += 1
            dfs(next_x,next_y)

for i in range(n):
    for j in range(n):
        if can_go(i,j):
            visited[i][j] = True
            cnt = 1
            dfs(i,j)

            ans.append(cnt)

print(len(ans))
ans.sort()
for i in ans:
    print(i)