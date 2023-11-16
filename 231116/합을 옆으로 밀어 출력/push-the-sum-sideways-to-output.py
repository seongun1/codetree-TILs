n=int(input())
tmp=0
for i in range(n):
    tmp +=int(input())
tmp = str(tmp)
tmp = tmp[1:] + tmp[0]
print(tmp)