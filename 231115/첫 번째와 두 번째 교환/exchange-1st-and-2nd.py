a =list(input())
x,y=a[0],a[1]
for i in range(len(a)):
    if a[i] == x:
        a[i] = y
    elif a[i] == y:
        a[i] =x
print(''.join(a))