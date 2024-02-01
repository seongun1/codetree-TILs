import sys

n = int(input())
arr = list(map(int,input().split()))

d = [0 for _ in range(n+1)] 

def init():
    for i in range(1,n+1):
        d[i] = -sys.maxsize

for i in range(1,n):
    for j in range(i):
        if d[i] == -sys.maxsize:
            continue
        
        if j + arr[j] >= i:
            d[i] = max(d[i], d[j] + 1)

print(max(d))