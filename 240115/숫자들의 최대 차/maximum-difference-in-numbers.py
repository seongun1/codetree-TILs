n,k = map(int,input().split())
arr=[int(input()) for _ in range(n)]
max_cnt =0
for i in range(1,10001):
    cnt =0
    for a in arr:
        if i <= a <= i+k:
            cnt +=1
    max_cnt = max(cnt,max_cnt)
print(max_cnt)