n=int(input())
arr= list(input().split())
for i in range(n):
    arr[i] = int(ord(arr[i]) - ord('A'))
cnt = 0
for i in range(1,n):
    for j in range(i,0,-1):
        if arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            cnt +=1
        else:
            break
print(cnt)