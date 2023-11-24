n=int(input())
arr=list(map(int,input().split()))
def gcd(a,b):
    if (a==0):
        return b
    return gcd(b%a,a)
def lcd(a,b):
    return int((a*b) / gcd(a,b))

if n>1:
    tmp = lcd(arr[0],arr[1])
    for i in range(2,n):
        tmp = lcd(tmp,arr[i])
    print(tmp)
else:
    print(arr[0])