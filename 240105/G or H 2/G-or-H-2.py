n=int(input())
arr=[0] * 101
for _ in range(n):
    a,b = input().split()
    a = int(a)
    arr[a] =b
max_dist =0
for i in range(101):
    for j in range(i,101):
        dist=0
        cnt_g,cnt_h =0,0
        if arr[i] == 0 or arr[j] == 0:
            continue
        for k in range(i,j+1):
            if arr[k]=='G':
                cnt_g +=1
            elif arr[k] =='H':
                cnt_h +=1
        if cnt_g ==0 or cnt_h==0 or cnt_g==cnt_h:
            dist = j-i
            max_dist = max(dist,max_dist)
print(max_dist)