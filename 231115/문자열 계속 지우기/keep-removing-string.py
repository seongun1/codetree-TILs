import sys
a=list(input())
b=list(input())
t=len(a)
tmp=''
i=0
while (i<=len(a)-len(b)):
    flag = False
    for j in range(len(b)):
        if a[i+j] == b[j]:
            flag = True
        else:
            flag = False
            break
    if flag:
        del a[i:i+j+1]
        i=0
    else:
        i+=1



print(''.join(a))