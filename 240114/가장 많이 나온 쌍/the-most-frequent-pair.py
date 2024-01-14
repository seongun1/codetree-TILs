n,m =map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
max_cnt =0
for a,b in arr:
    cnt =0
    for a1,b1 in arr:
        if (a == a1 and b == b1) or (a == b1 and  b==a1):
            cnt +=1 
    max_cnt = max(cnt,max_cnt)
print(max_cnt)