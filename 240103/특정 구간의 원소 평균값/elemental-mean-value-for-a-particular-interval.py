n=int(input())
arr=list(map(int,input().split()))
cnt =0
for i in range(n):
    for j in range(i,n):
        tmp,avg = 0,0
        for k in range(i,j+1):
            tmp += arr[k]
        avg = tmp / ((j+1) - i)
        if avg in arr[i:j+1]:
            cnt +=1
print(cnt)