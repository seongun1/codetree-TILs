n,k,t =input().split()
n= int(n)
k= int(k)
arr=[]
for i in range(n):
    arr.append(input())
result =[]
for a in arr:
    flag =True
    for i in range(len(t)):
        if a[i] != t[i]:
            flag = False
            break
    if flag:
        result.append(a)
result.sort()        
print(result[k-1])