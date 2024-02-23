n,m,x,y = map(int,input().split())

x -= 1
y -= 1

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

arr[x][y] = 1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for t in range(m):
    dist = 2 ** t

    new_arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for x in range(n):
        for y in range(n):
            if arr[x][y]:
                for dx,dy in zip(dxs, dys):
                    nx,ny = x+dx * dist, y+dy * dist

                    if not in_range(nx,ny):
                        continue
 
                    new_arr[nx][ny] = 1
    
    for x in range(n):
        for y in range(n):
            if new_arr[x][y]:
                arr[x][y] = 1

val = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            val += 1
print(val)