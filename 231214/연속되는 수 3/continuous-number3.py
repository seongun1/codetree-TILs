n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
tmp =[]
cnt =1
for i in range(1,n):
    if arr[i] * arr[i-1] < 0:
        cnt=1
    else:
        cnt +=1
        tmp.append(cnt)
print(max(tmp))