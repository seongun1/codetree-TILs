n=int(input())
x,y= n-1,n-1
arr=[[0]*n for _ in range(n)]
dxs=[0,-1,0,1]
dys=[-1,0,1,0]
cnt =n*n
arr[x][y] =cnt
dire =0
def in_range(x,y):
    return 0<=x<n and 0<=y<n

for _ in range(n*n-1):
    nx,ny = x+dxs[dire],y+dys[dire]
    if not in_range(nx,ny) or arr[nx][ny] !=0:
        dire = (dire+1)%4
    x,y =x+dxs[dire],y+dys[dire]
    cnt -=1
    arr[x][y] =cnt
for a in arr:
    for i in a:
        print(i,end=' ')
    print()