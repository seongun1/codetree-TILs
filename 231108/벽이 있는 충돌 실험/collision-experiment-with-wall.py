MAX_TIME = 100 # N의 최대가 50이여서

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
    
for _ in range(int(input())):
    n,m = map(int,input().split())

    arr = [[0] * n for _ in range(n)]

    for i in range(m):
        x,y,d = input().split()
        x,y = int(x),int(y)
        x -= 1
        y -= 1

        arr[x][y] = [1,d]
    
    # for i in arr:
    #     print(*i)
    # print('----')
    
    for _ in range(MAX_TIME):
        new_temp = [[0] * (n) for _ in range(n)]
        for x in range(n):
            for y in range(n):
                # 이동해서 또 해당 위치에 걸리는거 체크
                if arr[x][y] == 0:
                    continue

                nx,ny = x + dx[mapper[arr[x][y][1]]], y + dy[mapper[arr[x][y][1]]]

                if not in_range(nx,ny):
                    new_d = crash_with_wall(arr[x][y][1])
                    if new_temp[x][y] == 0:
                        new_temp[x][y] = [1,new_d]
                    else:
                        new_temp[x][y].append([1,new_d])
                    continue

                if new_temp[nx][ny] == 0:
                    new_temp[nx][ny] = arr[x][y]
                else:
                    new_temp[nx][ny].append(arr[x][y])

        # for i in new_temp:
        #     print(*i)
        # print('----new_temp----')

        for x in range(n):
            for y in range(n):
                #print("x : {}, y: {}, new_temp[x][y] : {}".format(x,y,new_temp[x][y]))
                if new_temp[x][y] == 0:
                    arr[x][y] = 0
                else:
                    if len(new_temp[x][y]) > 2:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = new_temp[x][y]
        # for i in arr:
        #     print(*i)
        # print('----after----')

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                cnt += 1
    print(cnt)