import copy
a = list(map(int,input()))
max_num =0

for i in range(len(a)):
    a[i] = 1-a[i]
    tmp=0
    for k in range(len(a)):
        tmp += a[len(a)-1-k] * (2**k)
    max_num = max(max_num,tmp)
    a[i] = 1-a[i]
print(max_num)