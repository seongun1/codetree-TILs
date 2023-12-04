n=int(input())
arr=[]
while (1):
    if n <2:
        arr.append(n)
        break
    arr.append(n%2)
    n //=2

arr= arr[::-1]
for a in arr:
    print(a,end='')