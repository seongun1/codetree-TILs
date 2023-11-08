import sys
n=int(input())
arr = list(map(int,input().split()))
max_num =0
index =0
arr.sort(reverse=True)
if n==1:
    print(arr[0])
    sys.exit()
while(arr[0] == arr[1] and arr[0] != -1):
    cnt =2
    while(1):
        if arr[0] == arr[cnt] and arr[0] != -1:
            cnt +=1
        else:
            break
    for i in range(0,cnt):
        arr[i] = -1
    arr.sort(reverse = True)
print(arr[0])