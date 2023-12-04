a,b = map(int,input().split())
n= input()
n = list(n)

def to_binary (a):
    ans =0
    for i in range(len(n)):
        n[i] = int(n[i])
        ans = ans *a +n[i]
    return ans
    
arr=[]
def from_binary(num,b):
    while (1):
        if num < b:
            arr.append(num)
            return
        arr.append(num % b)
        num //= b
t = to_binary(a)

from_binary(t,b)
for a in arr[::-1]:
    print(a,end='')