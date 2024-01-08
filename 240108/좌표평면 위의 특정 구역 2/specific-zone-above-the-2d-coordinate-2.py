import sys
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
max_x,max_y =0,0
min_x,min_y = 0,0
area=0
min_area =  sys.maxsize
for i in range(n):
    x,y=0,0
    max_x,max_y =0,0
    min_x,min_y = 40000,40000
    for j in range(n):
        if i==j:
            continue
        x,y= arr[j]
        max_x = max(x,max_x)
        max_y = max(y,max_y)
        min_x = min(x,min_x)
        min_y = min(y,min_y)
    area = (max_x - min_x) * (max_y - min_y)
    min_area = min(area,min_area)

print(min_area)