def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 상 하 좌 우
mapper = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3
}
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 방향 전환
def crash_with_wall(d):
    if d == 'U':
        d = 'D'
    elif d == 'D':
        d = 'U'
    elif d == 'L':
        d = 'R'
    elif d == 'R':
        d = 'L'
    return d
    

n,m,t,k = map(int,input().split())

arr = [[0] * n for _ in range(n)]
#arr = [[[] for _ in range(n)] for _ in range(n)]

for i in range(1,m+1):
    x,y,d,v = input().split()
    x,y,v = int(x),int(y),int(v)
    x -= 1
    y -= 1

    arr[x][y] = [1,d,v,i] # i는 번호다.

# print('---- 초기 arr ----')
# for i in arr:
#     print(*i)
# print('---- 초기 arr ----')

for _ in range(t):
    #new_temp = [[[] for _ in range(n)] for _ in range(n)]
    new_temp = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 이동해서 또 해당 위치에 걸리는거 체크
            if arr[x][y] == 0:
                continue

            speed = arr[x][y][2]
            nx,ny = x + dx[mapper[arr[x][y][1]]] * speed , y + dy[mapper[arr[x][y][1]]] * speed 

            if not in_range(nx,ny):
                arr[x][y][1] = crash_with_wall(arr[x][y][1])
                while 0 > nx or nx >= n or 0 > ny or ny >= n:
                    if nx < 0:
                        nx,ny = abs(nx),ny
                    elif ny < 0:
                        nx,ny = nx,abs(ny)
                    elif nx >= n:
                        nx,ny = 2*n-nx-2,ny
                    elif  ny >= n:
                        nx,ny = nx, 2*n-ny-2

            if new_temp[nx][ny] == 0:
                new_temp[nx][ny] = arr[x][y]
            else:
                new_temp[nx][ny].append(arr[x][y])
            
            # print('new temp array------')
            # for i in new_temp:
            #     print(*i)   
            # print('new temp array------')

    for x in range(n):
        for y in range(n):
            #tmp = [[] * n for _ in range(n)]
            tmp = []
            if new_temp[x][y] == 0:
                arr[x][y] = []
            else:

                #length = len(new_temp[x][y])

                #for i in range(length):
                # [1, 'D', 1, 0, [1, 'R', 3, 1], [1, 'U', 1, 2]] 이렇게 데이터가 들어온다.
                tmp.append(new_temp[x][y][:4])
                for j in new_temp[x][y][4:]:
                    tmp.append(j)
                new_temp[x][y] = tmp

                #print("new_temp[x][y] :", new_temp[x][y])

                if len(new_temp[x][y]) > k:
                    new_temp[x][y].sort(key=lambda x: (-x[2], -x[3]))
                    arr[x][y] = new_temp[x][y][:k]
                else:
                    arr[x][y] = new_temp[x][y]

# print('--------after --------')
# for i in arr:
#     print(*i)
# print('--------after --------')

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            cnt += len(arr[i][j])
print(cnt)