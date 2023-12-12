n=int(input())
arr= [[0] * 200 for i in range (200)]
tmp = [tuple(map(int,input().split())) for i in range(n)]
blue = False
for x1,y1,x2,y2 in tmp:
    x1,y1,x2,y2 = x1+100,y1+100,x2+100,y2+100
    for i in range(x1,x2):
        for j in range(y1,y2):
            if not blue:
                arr[i][j] = 1 #빨강
            else:
                arr[i][j] = 2
    if blue:
        blue = False
    else:
        blue =True
area =0
for a in arr:
    for i in a:
        if i==2:
            area +=1
print(area)