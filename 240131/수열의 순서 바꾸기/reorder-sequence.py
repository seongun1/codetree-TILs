n = int(input())
arr = list(map(int,input().split()))

cnt = 0
for i in range(n-2,-1,-1):
    if arr[i] > arr[i+1]:
        cnt = i + 1
        break
print(cnt)