a=input()
order = list(input())
for i in range(len(order)):
    if order[i] =='L':
        a=a[1:] + a[0]
    elif order[i] =='R':
        a=a[-1] + a[:-1]
print(a)