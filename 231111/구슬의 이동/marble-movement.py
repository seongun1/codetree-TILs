n, m, t, k = map(int, input().split())
arr = [[[] for _ in range(n)]for _ in range(n)]
next_arr = [[[] for _ in range(n)]for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

mapper = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}



def next_pos(x,y,v,direct):
    dx,dy = [-1,0,0,1], [0,1,-1,0]

    for _ in range(v):
        nx ,ny = x + dx[direct], y + dy[direct]

        if not in_range(nx,ny):
            direct = 3 - direct
            nx ,ny = x + dx[direct], y + dy[direct]
        x,y = nx,ny
    
    return (x,y,direct)


def move_all():
    for x in range(n):
        for y in range(n):
            for speed, idx, direct in arr[x][y]:
                next_x,next_y,next_dir = next_pos(x,y,speed,direct)
                new_arr[next_x][next_y].append((speed, idx, direct))

def simulate():
    for i in range(n):
        for j in range(n):
            if len(next_arr[i][j]) >= k:
                next_arr[i][j].sort(lambda x: (-x[0], -x[1]))
                while len(next_arr[i][j]) > k:
                    next_arr[i][j].pop()


for i in range(m):
    x, y, d, v = input().split()
    x,y,v = int(x),int(y),int(v)

    arr[x - 1][y - 1].append((v, i + 1, mapper[d]))


for _ in range(t):
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = []
		
    move_all()
    simulate()
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            cnt += len(arr[i][j])
print(cnt)