n=int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))
cnt =0
tmp=[]
for i in range(n):
    if i>=1 and arr[i-1] < arr[i]:
        cnt +=1
        tmp.append(cnt)
    else:
        cnt =1
        tmp.append(cnt)
print(max(tmp))