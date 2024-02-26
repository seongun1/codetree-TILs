n,m, t, k = map(int,input().split())

mapper = {
    "U" : 0,
    "R" : 1,
    "L" : 2,
    "D" : 3
}

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(1,m+1):
    x,y,d,v = input().split()
    x,y,v = int(x)-1, int(y)-1, int(v)
    arr[x][y].append([v, mapper[d], i]) # 속도, 방향, 번호

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(x,y,v,d):
    dx,dy = [1,0,0,-1], [0,1,-1,0]

    for _ in range(v):
        nx,ny = x + dx[d], y + dy[d]

        if not in_range(nx,ny):
            d = 3 - d
            nx,ny = x + dx[d], y + dy[d]
        x,y = nx,ny
    
    return (nx,ny,d)

def move_all():
    for i in range(n):
        for j in range(n):
            for v, direct, num in arr[i][j]:
                nx,ny,d = move(i,j,v,direct)
                temp[nx][ny].append([v,d,num])

def change(): # k개 이상인지 체크하고 물갈이
    for i in range(n):
        for j in range(n):
            if len(temp[i][j]) >= k:
                temp[i][j].sort(key = lambda x : (-x[0], -x[1]))
                while len(temp[i][j]) > k:
                    temp[i][j].pop()

for _ in range(t):
    temp =[
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    move_all()
    change()

    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

val = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            val += len(arr[i][j])
print(val)