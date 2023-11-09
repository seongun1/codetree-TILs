n,m = map(int,input().split())

def in_range(x,y):
    return 0<=x<n and 0<=y<n

tmp = []
for i in range(n):
    tmp.append(list(map(int,input().split())))

arr = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j].append(tmp[i][j])

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

changing_num = list(map(int,input().split()))

for num in changing_num:
    button = False

    for x in range(n):
        for y in range(n):
             #이때, 이 경우처럼 움직인 위치에 이미 다른 숫자가 있는 경우에는 해당 숫자들 중 가장 위에 위치하게 됩니다.
             #이동시 위에 있는 수들과 동시에 이동하는 문제입니다
            if len(arr[x][y]) == 0:
                continue
            
            if num in arr[x][y]:
                max_val = 0
                max_x,max_y = x,y

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if not in_range(nx, ny):
                        continue

                    if len(arr[nx][ny]) == 0:
                        continue

                    if max_val <= max(arr[nx][ny]):
                        max_val = max(arr[nx][ny])
                        max_x,max_y = nx,ny
                        
                # 새로 옮겨지면 기존의 숫자 위에 옮겨진다 => idx가 앞으로 채워진다
                idx = 0 
                for i, val in enumerate(arr[x][y]):
                    if val == num:
                        idx = i
                
                arr[max_x][max_y] = arr[x][y][:idx+1] + arr[max_x][max_y]
                # 옮겨진거 이후의 것들은 그대로 남아 있어야 한다 ( slicing의 범위 잘 체크 하기 )
                arr[x][y] = arr[x][y][idx+1:]

                button = True
                break

        if button:
            break

for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            print("None")
        else:
            print(*arr[i][j])