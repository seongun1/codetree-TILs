import sys
n=int(input())
arr=[int(input()) for _ in range(n)]

min_dist =sys.maxsize 
for i in range(n):
    dist =0
    for j in range(i+1,n):
        dist += abs(j-i) * arr[j]
    for j in range(i-1,-1,-1):
        dist += abs(n-(i-j)) * arr[j]
    min_dist = min(dist,min_dist)
print(min_dist)