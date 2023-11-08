n=int(input())
arr[1001]= [0] *1001
tmp = list(map(int,input().split()))
for i in range(n):
    arr[i] = tmp[i]
max_num =0
index =0
arr.sort(reverse=True)
while(1):
    if n==1:
        print(arr[n])
        break
    elif n==0:
        print(-1)
        break
    if arr[index] == arr[index+1]:
        index +=2
    else:
        print(arr[index])
        break
    
    if index >= n-1:
        print(-1)
        break