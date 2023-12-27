n,t = map(int,input().split())
arr=[[0]*n for _ in range(n)]
dx=[0,1,-1,0]
dy=[-1,0,0,1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

r,c,d = input().split()
r=int(r)-1
c=int(c)-1
mapper={'U':0,'D':3,'R':1,'L':2}
dire = mapper[d]
while (t>0):
    nr,nc = r+dy[dire],c+dx[dire]
    if not in_range(nr,nc):
        t-=1
        dire = 3-dire
    t-=1
    r,c=r+dy[dire],c+dx[dire]
print(r+1,c+1)