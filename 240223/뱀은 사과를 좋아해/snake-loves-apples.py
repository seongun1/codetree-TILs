from collections import deque

n,m,k = map(int,input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 사과 있는 장소
for _ in range(m):
    x,y = map(int,input().split())
    arr[x-1][y-1] = 2

# 방향 , 얼마나 움직일거야?
turn = []
whole = 0
for i in range(k):
    d,length = input().split()
    turn.append((d, int(length)))
    whole += int(length)

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 뱀의 위치
x,y = 0,0
q = deque()
time = 0
arr[x][y] = 1 # 뱀 위치
q.append((x,y))

move_dir = {
    'U' : 3,
    'D' : 2,
    'L' : 1,
    'R' : 0
}

# 동서남북
dx,dy = [0,-1,0,1], [1,0,-1,0]

def move():
    global x,y, time,k, whole

    if k == 0:
        return 0
    
    while True:
        
        for i in turn:
            direction, p = i

            if whole == 0:
                return time

            direct = move_dir[direction]

            for k in range(p):
                nx,ny = x + dx[direct], y + dy[direct]

                time += 1

                if not in_range(nx,ny):
                    return time

                if arr[nx][ny] == 2:
                    arr[nx][ny] = 1
                    q.append((nx,ny))

                elif arr[nx][ny] == 0 or arr[nx][ny]:
                    
                    hx,hy = q.popleft()
                    arr[hx][hy] = 0

                    if arr[nx][ny]:
                        return time

                    arr[nx][ny] = 1
                    q.append((nx,ny))
                
                
                x,y = nx,ny
                whole -= 1

move()
print(time)