x,y= 0,0
char=  input()
char=list(char)

dire = 0
dx= [0,1,0,-1]
dy = [-1,0,1,0]
for c in char:
    if c =='L':
        dire = (dire-1+4) %4
    elif c =='R':
        dire = (dire+1) %4
    elif c =='F':
        x,y= x+dx[dire] , y+dy[dire]
print(x,y)