n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if 0 in arr:
    ans = max((arr[0] * arr[1] * arr[-1]) ,(arr[-1] *arr[-2] * arr[-3]),0)
else:
    ans = max((arr[0] * arr[1] * arr[-1]) ,(arr[-1] *arr[-2] * arr[-3]))
print(ans)