import sys

n = int(input())
arr = list(map(int,input().split()))

d = [0] *n

def init():
    for i in range(n):
        d[i] = -sys.maxsize
    d[0] = 0

init()

for i in range(1,n):
    for j in range(i):
        # if d[i] == -sys.maxsize:
        #     continue
        
        if j + arr[j] >= i:
            d[i] = max(d[i], d[j] + 1)
#print(d)
print(max(d))