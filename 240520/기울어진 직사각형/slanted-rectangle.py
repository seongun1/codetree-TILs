n = int(input())

arr=[list(map(int,input().split())) for _ in range(n)]

def in_range(a,b):
    return 0<=a<n and 0<=b<n

def get_score(x,y,width,height):
    dxs,dys = [-1,-1,1,1],[1,-1,-1,1]
    move_nums = [width,height,width,height]

    ans = 0
    for dx,dy,move_num in zip(dxs,dys,move_nums):
        for _ in range(move_num):
            x,y = x+dx,y+dy
            if not in_range(x,y):
                return 0
            ans += arr[x][y]
    return ans
ans = 0
for i in range(n):
    for j in range(n):
        for width in range(1,n):
            for height in range(1,n):
                ans = max(ans,get_score(i,j,width,height))
print(ans)