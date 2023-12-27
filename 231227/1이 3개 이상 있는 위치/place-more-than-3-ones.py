n=int(input())
arr= []
for _ in range(n):
    arr.append(list(map(int,input().split())))
dxs =[0,0,1,-1]
dys =[1,-1,0,0]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
ans =0
for i in range(n):
    for j in range(n):
        cnt =0
        for dx,dy in zip(dxs,dys):
            nx ,ny=i+dx,j+dy
            if in_range(nx,ny) and arr[nx][ny] ==1:
                cnt +=1
        if cnt >=3:
            ans +=1
print(ans)