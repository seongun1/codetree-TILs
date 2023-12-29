n,m = map(int,input().split())
dxs=[1,0,-1,0]
dys =[0,1,0,-1]
arr=[[0]*m for i in range(n)]

cnt=2
def in_range(x,y):
    return 0<=x <n and 0<=y<m
x,y=0,0
dire= 0
arr[x][y] =1
for _ in range(n*m-1):
    nx,ny = x+dxs[dire],y+dys[dire]
    if not in_range(nx,ny) or arr[nx][ny] !=0:
        dire = (dire+1) % 4
    x,y = x+dxs[dire],y+dys[dire]
    arr[x][y] = cnt
    cnt +=1
for a in arr:
    for i in a:
        print(i,end=' ')
    print()