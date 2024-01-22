n,k = map(int,input().split())
arr = list(map(int,input().split()))
import sys

budget = 0

def is_possible(num,k):
    budget =0
    for j in range(n):
        if num<= arr[j] <= num+k:
            continue
        budget += min(abs(num-arr[j]),abs(num+k - arr[j]))
    return budget
max_budget =sys.maxsize
for point in range(10001):
    max_budget = min(is_possible(point,k),max_budget)

print(max_budget)