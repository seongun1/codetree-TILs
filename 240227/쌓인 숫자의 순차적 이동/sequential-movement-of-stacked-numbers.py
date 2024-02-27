n,m = map(int,input().split())

dxs,dys = [-1,-1,-1,0,1,1,1,0], [-1,0,1,1,1,0,-1,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

tmp = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

moving = list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        arr[i][j].append(tmp[i][j])

# (-1,-1)이 반환되면 멈추기
def next_pos(x,y):
    cur_x, cur_y, max_val = x,y,0
    
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy

        if not in_range(nx,ny):
            continue

        if arr[nx][ny] == []:
            continue
        
        if max(arr[nx][ny]) >= max_val:
            max_val = max(arr[nx][ny])
            cur_x, cur_y = nx,ny

    return cur_x, cur_y        

for val in moving:
    flag = False

    for i in range(n):
        for j in range(n):

            if val not in arr[i][j]:
                continue

            nx,ny = next_pos(i,j)

            idx = 0
            for h, num in enumerate(arr[i][j]):
                if val == num:
                    idx = h
            
            arr[nx][ny] = arr[i][j][:idx+1] + arr[nx][ny]
            arr[i][j] = arr[i][j][idx+1:]

            flag = True
            break
        
        if flag:
            break


for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            print("None")
        else:
            print(*arr[i][j])