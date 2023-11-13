n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
cnt =0
tmp =0
for a in arr:
    tmp += len(a)
    if a[0] == 'a':
        cnt +=1
print (tmp,cnt)