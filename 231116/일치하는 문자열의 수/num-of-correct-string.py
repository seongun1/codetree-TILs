n,a=input().split()
n=int(n)
cnt =0
for i in range(n):
    tmp =input()
    if a==tmp:
        cnt +=1
print(cnt)