from collections import deque

n,k = map(int,input().split())
arr = deque()
ans =[]
for i in range(1,n+1):
    arr.append(i)
while arr:
    for i in range(k-1):
        val = arr.popleft()
        arr.append(val)
    ans.append(arr.popleft())
for a in ans:
    print(a,end=' ')