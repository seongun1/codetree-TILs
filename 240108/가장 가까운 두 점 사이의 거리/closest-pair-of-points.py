import sys
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
min_dist =sys.maxsize
dist=sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        dist = (arr[i][0] - arr[j][0]) **2 + (arr[i][1] - arr[j][1])**2
        min_dist =min (dist, min_dist)
print(min_dist)