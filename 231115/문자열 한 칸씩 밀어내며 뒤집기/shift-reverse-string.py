a,b=input().split()
b=int(b)
for i in range(b):
    tmp = int(input())
    if tmp ==1:
        a=a[1:] + a[0]
        print(a)
    elif tmp ==2:
        a=a[-1] + a[:-1]
        print(a)
    elif tmp ==3:
        a=a[::-1]
        print(a)