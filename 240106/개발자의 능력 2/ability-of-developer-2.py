import sys
arr=list(map(int,input().split()))
n= len(arr)
arr.sort()
ans =[]
for i in range(1,3):
    tmp = arr[i] + arr[-i-1]
    ans.append(tmp)

print(max(ans) - min(ans))