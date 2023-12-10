n=int(input())
arr=[[0 for _ in range(100)]for _ in range(100)]
for _ in range(n):
    x1,y1,x2,y2= map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = 1
area = 0
for a in arr:
    for i in a:
        if i == 1:
            area +=1
print(area)