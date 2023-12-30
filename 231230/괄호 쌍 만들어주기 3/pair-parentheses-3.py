a = input()
a = list(a)
closed = False
cnt =0
for i in range(len(a)):
    if a[i] == '(':
        closed =True
    if closed:
        for j in range(i,len(a)):
            if a[j] ==')':
                cnt +=1
        closed =False
print(cnt)