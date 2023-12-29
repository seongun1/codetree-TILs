n,t = map(int,input().split())


order =input()
order = list(order)
arr=[list(map(int,input().split())) for _ in range(n)]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
dire =0
dxs=[-1,0,1,0]
dys=[0,1,0,-1]
x,y=n//2,n//2
tmp = arr[x][y]
for o in order:
    if o =='L':
        dire = (3+dire) % 4
    elif o =='R':
        dire = (dire+1) % 4
    else:
        nx,ny = x+dxs[dire],y+dys[dire]
        if in_range(nx,ny):
            x,y = nx,ny
        else:
            continue
        tmp +=arr[x][y]
print(tmp)