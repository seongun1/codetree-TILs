import sys
n=int(input())
arr=list(map(int,input().split()))
min_num =sys.maxsize
for i in range(n):
    tmp=0
    for j in range(n):
        tmp += abs(j-i)*arr[j]
    min_num = min(tmp,min_num)
print(min_num)