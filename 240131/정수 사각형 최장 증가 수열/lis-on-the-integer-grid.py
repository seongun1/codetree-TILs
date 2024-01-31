n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

max_val = 0

def dfs(x,y):
    global max_val
    #print(x,y , max_val)
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if in_range(next_x,next_y) and arr[next_x][next_y] > arr[x][y]:
            d[next_x][next_y] = d[x][y] + 1
            max_val = max(max_val, d[next_x][next_y])
            dfs(next_x, next_y)
        

for x in range(n):
    for y in range(n):
        d = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        d[x][y] = 1
        dfs(x,y)

print(max_val)