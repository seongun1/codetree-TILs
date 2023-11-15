a=list(input())
b=a[1]
c=a[0]
for i in range(len(a)):
    if a[i] == b:
        a[i] =c
print(''.join(a))