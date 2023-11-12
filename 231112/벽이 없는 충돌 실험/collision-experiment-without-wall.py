import sys
input = sys.stdin.readline

tmp, crash_time = None, None
arr = [[None for _ in range(4001)] for __ in range(4001)]
OFF_SET = 1000
dx,dy = [-1,0,0,1], [0,-1,1,0]
coords = []

mapper = {
    "U" : 0,
    "R" : 1,
    "L" : 2,
    "D" : 3
}

def in_range(x,y):
    return 0<=x<4001 and 0<=y<4001

# 이동만 고려
def move_all():
    global tmp, coords
    crash = False
    coords.clear()

    for i in range(len(tmp)):
        idx,x,y,w,d = tmp[i]

        nx,ny = x + dx[d] , y + dy[d]

        if not in_range(nx,ny):
            continue
        
        if arr[nx][ny] == None:
            arr[nx][ny] = [idx,nx,ny,w,d]
            coords.append((nx,ny))
        else:
            crash = True
            if arr[nx][ny][3] > w:
                continue
            if arr[nx][ny][3] == w and arr[nx][ny][0] > idx:
                continue
            arr[nx][ny] = [idx, nx, ny, w, d]

    
    tmp.sort()
    for x,y in coords:
        tmp.append(arr[x][y])
        arr[x][y] = None
    return crash


for _ in range(int(input())):
    n = int(input()) # 구슬 개수
    tmp = []
    crash_time = -1 

    for i in range(1,n+1):
        tmp.append(
            [i] + \
            list(map(lambda x: (int(x[1])+OFF_SET)*2 if x[0]==0 or x[0]==1 \
                        else int(x[1]) if x[0]==2 \
                        else mapper[x[1]], enumerate(input().split())))
        )

    for time in range(4001):
        if move_all():
            crash_time = time + 1
    
    print(crash_time)