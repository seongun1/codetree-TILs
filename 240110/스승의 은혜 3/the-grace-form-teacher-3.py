n,b = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

arr = sorted(arr,key =lambda x : x[0]+x[1])
budget = b
max_cnt =0
for i in range(n):
    arr[i][0] /= 2
    price,cnt = 0,0
    for j in range(n):
        price = arr[j][0] + arr[j][1]
        budget -= price
        if budget>=0:
            cnt +=1
        else:
            budget += price
    max_cnt = max(cnt,max_cnt)
    arr[i][0] *=2
    budget =b
print(max_cnt)