n=int(input())
arr= [0 for _ in range(1001)]
tmp = list(map(int,input().split()))
for i in range(n):
    arr[i] = tmp[i]
max_num =0
index =0
arr.sort(reverse=True)
while(1):
    if n==1:
        print(arr[0])
        break
    elif n==0:
        print(-1)
        break
    if arr[index] == arr[index+1]:
        index +=2
        continue
    else:
        print(arr[index])
        break
    
    if index >= n-1:
        print(-1)
        break