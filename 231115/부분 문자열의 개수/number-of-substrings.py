a=input()
b=input()
cnt =0
for i in range(len(a) - len(b) +1):
    flag = True
    for j in range(len(b)):
        if a[i+j] != b[j]:
            flag = False
    if flag:
        cnt +=1
print(cnt)