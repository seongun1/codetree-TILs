n=int(input())
arr= list(input().split())
for i in range(n):
    arr[i] = int(ord(arr[i]) - ord('A'))
cnt = 0
while (1):
    flag = True
    for i in range(n):
        if arr[i] != i:
            flag =False
            cnt +=1
            if abs(i-arr[i]) > abs(i+1 - arr[i]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
            else:
                arr[i],arr[i-1] < arr[i-1],arr[i]
    if flag:
        break
print(cnt)