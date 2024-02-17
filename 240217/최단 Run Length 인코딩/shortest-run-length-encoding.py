import sys

arr = list(input())
n = len(arr)

ans = sys.maxsize

def right_shift():
    tmp = arr[-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = tmp

def press():
    #print(arr)
    compress = ""
    cnt = 1

    if n == 1 or n == 2:
        return 2

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            cnt += 1
        else:
            compress += arr[i] + str(cnt)
            cnt = 1
        
        if i == n-2:
            compress += arr[i+1] + str(cnt)

    return len(compress)

for _ in range(n):

    ans = min(ans, press())
    right_shift()
print(ans)