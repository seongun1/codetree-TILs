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
            for j in range(n):
                if arr[i] == j:
                    arr[i],arr[j] = arr[j],arr[i]
    if flag:
        break
print(cnt)