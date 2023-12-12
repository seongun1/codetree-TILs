n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
cnt =0
tmp =[]
for i in range(n):
    if i==0 or arr[i] == arr[i-1]:
        cnt +=1
        tmp.append(cnt)
    else:
        cnt =1
print(max(tmp))