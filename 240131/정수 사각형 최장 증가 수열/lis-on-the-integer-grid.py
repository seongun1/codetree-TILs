n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_cnt = 0

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global cnt
    tmp = 0
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx , y + dy

        if not in_range(next_x, next_y):
            cnt.append(tmp)
            tmp = 0
            continue
        
        if arr[x][y] >= arr[next_x][next_y]:
            cnt.append(tmp)
            tmp = 0
            continue
        
        # if visited[next_x][next_y]:
        #     continue

        #print("arr[x][y] : {}, arr[next_x][next_y] : {}".format(arr[x][y], arr[next_x][next_y]))
        tmp += 1
        #visited[next_x][next_y] = True
        dfs(next_x, next_y)
    cnt.append(tmp)

for x in range(n):
    for y in range(n):
        cnt = []
        
        # visited = [
        #     [False for _ in range(n)]
        #     for _ in range(n)
        # ]

        # visited[x][y] = True
        dfs(x,y)

        #print(x,y,cnt)

        max_cnt = max(max_cnt,max(cnt))

print(max_cnt+1)