n,b = map(int,input().split())
arr=[]
def chage_num(n,b):
    while (1):
        if n < b:
            arr.append(n)
            return
        arr.append(n%b)
        n //=b
chage_num(n,b)
for a in arr[::-1]:
    print(a,end='')