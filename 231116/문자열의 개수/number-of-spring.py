cnt =0
arr=[]
while(1):
    tmp =input()
    if tmp =='0':
        break
    cnt +=1
    if cnt %2:
        arr.append(tmp)
print(cnt)
for a in arr:
    print(a)