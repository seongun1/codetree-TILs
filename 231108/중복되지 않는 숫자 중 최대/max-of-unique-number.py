n=int(input())
arr= list(map(int,input().split()))
max_num =0
index =0
arr.sort(reverse=True)
while(1):
    if n==1:
        print(arr[n])
        break
    if arr[index] == arr[index+1]:
        index +=2
    else:
        print(arr[index])
        break
    if index >= n-1:
        print(-1)
        break