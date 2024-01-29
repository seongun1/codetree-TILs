n,m = map(int,input().split())
arr= list(map(int,input().split()))
cnt =0
point =0
while(1):
    if arr[point] ==1:
        for i in range(point+1,n):
            if arr[i] == 1 and i - point <=m:
                continue
            elif arr[i] ==1 and i - point >m:
                cnt +=1
                point = i
    else:
        point +=1
    if point == n-1:
        break
print(cnt)