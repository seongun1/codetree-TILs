n,t = map(int,input().split())
arr=[[0]*n for _ in range(n)]
dx=[-1,0,0,1]
dy= [0,1,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

x,y,d = input().split()
x=int(x)-1
y=int(y)-1
mapper={'U':0,'D':3,'R':1,'L':2}
dire = int(mapper[d])

for i in range(t):
    nx,ny = x+dx[dire],y+dy[dire]
    if not in_range(nx,ny):
        dire = 3- dire
    else:
        x,y = nx,ny
print(x+1,y+1)