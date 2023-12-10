x1,y1,x2,y2 =map(int,input().split())
x11,y11,x22,y22 =map(int,input().split())
x111,y111,x222,y222=map(int,input().split())
area = [[0 for i in range(2000)]for i in range(2000)]
for i in range(x1,x2): #A의 넓이
    for j in range(y1,y2):
        area[i][j] =1
for i in range(x11,x22): #B의 넓이
    for j in range(y11,y22):
        area[i][j] =1
#겹치는 구간?
for i in range(x111,x222):
    for j in range(y111,y222):
        area[i][j] =0
cnt = 0
for a in area:
    for i in a:
        if i ==1:
            cnt +=1
print(cnt)