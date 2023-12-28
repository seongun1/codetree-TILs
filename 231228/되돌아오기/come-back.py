n=int(input())
dire ={'W':0,'S':1,'N':2,'E':3}
arr= [[0]*2001 for _ in range(2001)]
dxs=[0,1,-1,0]
dys=[-1,0,0,1]

def function(n):
    time =0
    ans =0
    x,y = 1000,1000
    for _ in range(n):
        d,t = input().split()
        direction = dire[d]
        t=int(t)
        for _ in range(time,time+t):
            x,y=x+dxs[direction],y+dys[direction]
            ans +=1
            if x==1000 and y == 1000:
                return ans
            time +=t
    return -1
print(function(n))