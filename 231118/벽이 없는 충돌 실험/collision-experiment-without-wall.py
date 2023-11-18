import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

mapper = {
    "U": 0,
    "R": 1,
    "D": 2,
    "L": 3
}

grid = [[None for _ in range(4001)] for __ in range(4001)]
OFFSET_1 = 1000
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
coords = []

def in_range(x,y):
    return 0<=x<4001 and 0<=y<4001

# 구슬들을 움직이는 함수
def move():
    global marbles, coords # [] [] 
    crash = False
    coords.clear()

    for i in range(len(marbles)):
        idx, x, y, w, d = marbles[i]
        nx, ny = x + dx[d], y + dy[d]

        if not in_range(nx,ny):
            continue

        # 나중에 grid 배열 초기화할때 기록한 부분만 지우기 위해 따로 좌표 기억해두기    
        if grid[nx][ny] == None:
            grid[nx][ny] = [idx, nx, ny, w, d]
            coords.append((nx, ny))
        else:
            crash = True
            if grid[nx][ny][3] > w:
                continue
            if grid[nx][ny][3] == w and grid[nx][ny][0] > idx:
                continue
            grid[nx][ny] = [idx, nx, ny, w, d]

    marbles.clear()
    for x, y in coords:
        marbles.append(grid[x][y])
        grid[x][y] = None

    return crash   

def get_max_min_pos(x, y):
    global max_x, max_y, min_x, min_y

    if x > max_x : 
        max_x = x
    elif x < min_x :
        min_x = x
    
    if y > max_y : 
        max_y = y
    elif y < min_y :
        min_y = y

for _ in range(int(input())):
    N = int(input())

    max_x, max_y = INT_MIN, INT_MIN 
    min_x, min_y = INT_MAX, INT_MAX

    marbles, record = [], -1
    for i in range(1,N+1):
        x,y,w,d = input().split()
        marbles.append( [i,(int(x) + OFFSET_1)*2,(int(y) + OFFSET_1)*2,int(w),mapper[d]] )
        get_max_min_pos((int(x) + OFFSET_1) * 2, (int(y) + OFFSET_1) * 2)

    max_time = max( (max_x - min_x), (max_y - min_y) )

    for second in range(max_time):
        if move():
            record = second+1

    print(record)