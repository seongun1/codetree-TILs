a,b = map(int,input().split())
c,d =map(int,input().split())

arr=[0] * 101
for i in range(a,b):
    arr[i] = 1
for k in range(c,d):
    arr[k] = 1
ans =0
for a in arr:
    if a ==1:
        ans +=1
print(ans)