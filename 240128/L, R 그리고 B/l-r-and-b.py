arr=[]
def in_range(x,y):
    return 0<=x<10 and 0<=y<10

for _ in range(10):
    tmp = str(input())
    arr.append(list(tmp))

dx =[-1,1,0,0]
dy = [0,0,-1,1]
cnt =0
idx_b,idy_b,idx_r,idy_r=0,0,0,0
x,y = 0,0
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            idx_b,idy_b = i,j
        if arr[i][j] == 'R':
            idx_r,idy_r = i,j
        if arr[i][j] == 'L':
            x,y = i,j
while (1):
    for a,b in zip(dx, dy):
        nx = x+a
        ny = y+b
        if in_range(nx,ny) and abs(nx - idx_b) <= abs(x - idx_b) and abs(ny - idy_b) <= abs(y - idy_b) and arr[nx][ny] != 'R':
            x = x+a
            y = y+b
            break
    if arr[nx][ny] == 'B':
        break
    cnt +=1
    
print(cnt)