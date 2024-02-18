n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

x, y ,m1, m2, m3, m4, direct = map(int, input().split())
move_num = [m1, m2, m3, m4]

r = x - 1
c = y - 1

def shift():
    global r, c, m1, m2, m3, m4, direct, arr

    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    tmp = arr[r][c]
    cx,cy = r,c

    for d in range(4):
        move = move_num[d]

        for _ in range(move):
            nx,ny = cx + dxs[d] , cy + dys[d]
            arr[cx][cy] = arr[nx][ny]
            cx,cy = nx,ny
    
    arr[r-1][c-1] = tmp

def reverse_shift():
    global r, c, m1, m2, m3, m4, direct, arr

    dxs = [1, 1, -1, -1]
    dys = [-1, 1, 1, -1]
    tmp = arr[r][c]
    cx,cy = r,c

    for d in range(3,-1,-1):
        move = move_num[d]

        for _ in range(move):
            nx,ny = cx + dxs[d] , cy + dys[d]
            arr[cx][cy] = arr[nx][ny]
            cx,cy = nx,ny
    
    arr[r-1][c+1] = tmp

if direct == 1: # 시계
    shift()
else:
    reverse_shift()

for i in arr:
    print(*i)