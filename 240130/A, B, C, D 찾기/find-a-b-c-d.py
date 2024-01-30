arr=list(map(int,input().split()))
arr.sort()
#print(arr)
a = arr[0]
b = arr[1]
if a+b == arr[2]:
    c = arr[3]
else:
    c = arr[2]
d = arr[-1] -(a+b+c)
print(a,b,c,d)