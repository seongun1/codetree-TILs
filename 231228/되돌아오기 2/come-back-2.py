x,y=0,0
tmp=input()
tmp=list(tmp)
dxs=[-1,0,1,0]
dys =[0,1,0,-1]
dire =0
time =0
def move(x,y):
    global dire
    global time
    for t in tmp:
        if t=='L':
            dire = (dire+3)%4
            time +=1
        elif t =='R':
            dire =(dire+1)%4
            time+=1
        elif t=='F':
            x,y = x+dxs[dire],y+dys[dire]
            time +=1
        if x==0 and y ==0:
            return time
    return -1

print(move(x,y))