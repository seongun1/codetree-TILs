import copy
a = list(map(int,input()))
max_num =0

for i in range(len(a)):
    num = copy.deepcopy(a)
    tmp=0
    if a[i] ==0:
        num[i] = 1
    elif a[i] ==1:
        num[i] = 0
    for k in range(len(num)):
        tmp += num[len(num)-1-k] * (2**k)
    max_num = max(max_num,tmp)
print(max_num)