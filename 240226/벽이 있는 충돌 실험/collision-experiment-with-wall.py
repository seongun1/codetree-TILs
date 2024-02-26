# 상하 좌우
dxs,dys = [-1,1,0,0], [0,0,-1,1]

MAX_TIME = 100

mapper = {
    "U" : 0,
    "D" : 1,
    "L" : 2,
    "R" : 3
}

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def crack(d):
    if d % 2 == 0:
        d += 1
    else:
        d -= 1
    return d

def move(x,y,d):
    nx,ny = x + dxs[d], y + dys[d]

    if not in_range(nx,ny):
        direct = crack(d)
        return x,y,direct
    else:
        return nx,ny, d


for tc in range(int(input())):
    n,m = map(int,input().split())

    coords = list()
    for _ in range(m):
        x,y,direct = input().split()
        x,y = int(x) - 1, int(y) - 1
        coords.append((x, y, direct))
    
    arr = [
        [0] * n
        for _ in range(n)
    ]

    for i in coords:
        x,y,d = i
        arr[x][y] = [1, mapper[d]] # 공이 있는 곳

    for _ in range(MAX_TIME):
        temp = [
            [0] * n
            for _ in range(n)
        ]

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    continue

                nx,ny,d = move(i,j,arr[i][j][1])

                if temp[nx][ny] == 0:
                    temp[nx][ny] = [1,d]
                else:
                    temp[nx][ny].append([1,d])
        
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 0:
                    arr[i][j] = temp[i][j]
                    continue
                    
                elif len(temp[i][j]) >= 3:
                    temp[i][j] = 0
                arr[i][j] = temp[i][j]

    val = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                val += 1
    print(val)