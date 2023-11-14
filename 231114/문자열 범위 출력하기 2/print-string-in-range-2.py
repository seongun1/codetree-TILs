a = input()
b=int(input())
a=a[::-1]
if b>=len(a):
    print(a)
else:
    for i in range(b):
        print(a[i],end='')