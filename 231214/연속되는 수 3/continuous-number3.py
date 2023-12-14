n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
tmp =[]
cnt =0
ans =0
for i in range(n):
    if i>=1 and arr[i] * arr[i-1] >0:
        cnt +=1
        tmp.append(cnt)
    else:
        cnt =1
        tmp.append(cnt)
print(max(tmp))