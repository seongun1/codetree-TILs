a=input()
b=input()
cnt =0
while (cnt <= len(a)):
    cnt +=1
    a = a[1:] + a[0]
    if a==b:
        break
if cnt > len(a):
    cnt = -1
print(cnt)