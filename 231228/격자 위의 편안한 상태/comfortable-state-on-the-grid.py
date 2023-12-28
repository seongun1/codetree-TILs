n,m = map(int,input().split())
arr=[[0]*(n) for _ in range(n)]
dxs=[-1,0,1,0]
dys =[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def is_comfortable(x,y):
    arr[x][y] =1
    cnt=0
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx,y+dy
        if in_range(nx,ny) and arr[nx][ny] ==1:
            cnt +=1
    if cnt ==3:
        return 1
    else:
        return 0

for _ in range(m):
    x,y= map(int,input().split())
    print(is_comfortable(x-1,y-1))