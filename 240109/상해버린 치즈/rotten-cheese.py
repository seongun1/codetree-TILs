n,m,d,s = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(d)] #p,m,t
arr2 = [list(map(int,input().split())) for _ in range(s)] #p,t
max_cnt =0
for i in range(1,m+1):
    time = [0] *(n+1)
    for a in arr1:
        if a[1] != i:
            continue
        person = a[0]
        if time[person] ==0:
            time[person] = a[2]
        elif time[person] > a[2]:
            time[person] = a[2]
    flag = True
    for b in arr2:
        person = b[0]
        if time[person] ==0:
            flag =False
        if time[person] >= b[1]:
            flag =False
    cnt =0
    if flag:
        for j in range(1,n+1):
            if time[j] != 0:
                cnt +=1

    max_cnt = max(cnt,max_cnt)
print(max_cnt)