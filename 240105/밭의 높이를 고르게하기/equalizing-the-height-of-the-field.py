import sys
n,h,t =map(int,input().split())
arr=list(map(int,input().split()))
min_cost=sys.maxsize
for i in range(n-t+1):
    cost=0
    for j in range(i,i+t):
        cost += abs(arr[j]-h)
    min_cost = min(cost,min_cost)
print(min_cost)