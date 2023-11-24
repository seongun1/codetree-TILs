n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for a in arr:
    print(a,end=' ')
arr= list(reversed(arr))
print()
for a in arr:
    print(a,end=' ')