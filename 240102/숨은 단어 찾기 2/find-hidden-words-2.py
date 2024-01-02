n,m = map(int,input().split())
arr=[]
for _ in range(n):
    tmp = input()
    arr.append(list(tmp))
def in_range(x,y):
    return 0<=x<n and 0<=y<m
dxs =[0,1,1,1,0,-1,-1,-1]
dys =[1,1,0,-1,-1,-1,0,1]
cnt=0
for i in range(n):
    for j in range(m):
        if arr[i][j] =='L':
            x,y = i,j
            for dx,dy in zip(dxs,dys):#8방향 탐색
                nx ,ny = x+dx,y+dy
                if in_range(nx,ny) and arr[nx][ny] =='E':
                    kx=nx
                    ky=ny
                    nx,ny =kx+dx,ky+dy
                    if in_range(nx,ny) and arr[nx][ny] =='E':
                            cnt +=1
print(cnt)