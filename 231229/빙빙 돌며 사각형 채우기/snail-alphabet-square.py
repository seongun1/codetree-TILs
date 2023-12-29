n,m = map(int,input().split())
mapper = {
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
    6 : 'G',
    7 : 'H',
    8 : 'I',
    9 : 'J',
    10 : 'K',
    11 : 'L',
    12 : 'M',
    13 : 'N',
    14 : 'O',
    15 : 'P',
    16 : 'Q',
    17 : 'R',
    18 : 'S',
    19 : 'T',
    20 : 'U',
    21 : 'V',
    22 : 'W',
    23 : 'X',
    24 : 'Y',
    25 : 'Z',
}
def in_range(x,y):
    return 0<=x<n and 0<=y<m
dire= 0
arr=[[0]*m for _ in range(n)]
dxs = [0,1,0,-1]
dys =[1,0,-1,0]
x,y= 0,0
cnt=0
arr[x][y] = mapper[cnt]
for i in range(n*m-1):
    nx,ny = x+dxs[dire],y+dys[dire]
    if not in_range (nx,ny) or arr[nx][ny] != 0:
        dire = (dire+1) %4
    x,y = x+dxs[dire],y+dys[dire]
    cnt = (cnt+1) % 26
    arr[x][y] = mapper[cnt]
for a in arr:
    for i in a:
        print(i,end=' ')
    print()