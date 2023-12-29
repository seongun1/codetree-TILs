n=int(input())
arr=[list(input())for _ in range(n)]

k=int(input())
dxs = [1,0,-1,0]
dys = [0,-1,0,1]
dire,x,y =0,0,0

if k<=n:
    dire,x,y =0,0,k-1
elif n<k and k<=2*n:
    dire,x,y = 1,k-n-1,n-1
elif 2*n < k and k<=3*n:
    dire,x,y= 2,n-1,n-(k-2*n)
elif 3*n <k and k<=4*n:
    dire,x,y=3,n-(k-3*n),0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

slash ={0:1,1:0,2:3,3:2}
de_slash ={0:3,1:2,2:1,3:0}
ans =0
while in_range(x,y):
    if arr[x][y] =='/':
        dire = slash[dire]
    elif arr[x][y] == '\\':
        dire = de_slash[dire]
    x,y = x+dxs[dire],y+dys[dire]
    ans +=1
print(ans)