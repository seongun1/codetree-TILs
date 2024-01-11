n=int(input())
arr=[0] * 102
for i in range(n):
    arr[i] = int(input())
top = max(arr)
max_cnt,cnt =0,0

for i in range(top+1):
    cnt =0
    for j in range(n+1):
        if arr[j] -i >0 and arr[j+1] - i <=0:
            cnt +=1
    max_cnt = max(cnt,max_cnt)
print(max_cnt)