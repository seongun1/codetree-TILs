n=int(input())
arr =list(map(int,input().split()))
arr.sort()
tmp = []

for i in range(n):
    tmp.append([arr[i],arr[i+n]])
import sys
ans = sys.maxsize
for a,b in tmp:
    ans = min(ans,b-a)
print(ans)