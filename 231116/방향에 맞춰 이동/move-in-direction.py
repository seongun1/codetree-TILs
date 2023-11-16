n=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
x,y= 0,0
for i in range(n):
    tmp = input().split()
    tmp[1] = int(tmp[1])
    if tmp[0] =='N':
        for j in range(tmp[1]):
            x,y= x+dx[0],y+dy[0]
    elif tmp[0] == 'E':
        for j in range(tmp[1]):
            x,y = x+dx[2] , y+dy[2]
    elif tmp[0] == 'S':
        for j in range(tmp[1]):
            x,y = x+dx[1] ,y+dy[1]
    elif tmp[0] == 'W':
        for j in range(tmp[1]):
            x,y = x+dx[3],y+dy[3]
print(x,y)