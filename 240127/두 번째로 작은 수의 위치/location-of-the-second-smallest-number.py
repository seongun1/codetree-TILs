n=int(input())
arr=list(map(int,input().split()))
import sys
min_val = sys.maxsize
idx = -1
for i in range(n):
    if arr[i] <min_val:
        min_val = arr[i]
val =sys.maxsize
flag =False
for i in range(n):
    if arr[i] == val and flag:
        idx = -1
    if min_val<arr[i]<val:
        val = arr[i]
        idx = i+1
        flag =True

print(idx)