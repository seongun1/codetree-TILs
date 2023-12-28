n,m =map(int,input().split())
def in_range(x,y):
    return 0<=x<n and 0<=y<m
arr=[[0]*m for _ in range(n)]
x,y = 0,0
dxs=[0,1,0,-1]
dys =[1,0,-1,0]
arr[x][y] = 1
dire =0
for i in range(2,n*m+1):
    nx,ny = x+dxs[dire],y+dys[dire]
    if not in_range(nx,ny) or not arr[nx][ny] ==0:
        dire = (dire+1)%4
    x,y = x+dxs[dire],y+dys[dire]
    arr[x][y] = i
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()