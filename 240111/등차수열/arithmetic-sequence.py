n=int(input())
arr=list(map(int,input().split()))
arr.sort()
max_cnt =0
for i in range(1,101):
    cnt =0
    for j in range(n):
        for k in range(j+1,n):
            if i - arr[j] == arr[k] - i:
                cnt +=1
    max_cnt = max(cnt,max_cnt)
print(max_cnt)