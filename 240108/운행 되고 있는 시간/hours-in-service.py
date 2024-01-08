n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
max_cnt=0
for i in range(n):
    run_time=[0] *1001
    for j in range(n):
        if i==j:
            continue
        a,b = arr[j]
        for k in range(a,b):
            run_time[k] +=1
    cnt=0
    for t in run_time:
        if t >= 1:
            cnt +=1
    max_cnt = max(cnt,max_cnt)
print(max_cnt)