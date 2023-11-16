a,b=input().split()
for i in range(len(a)):
    if not a[i].isdigit():
        a=a[:i]
        break
for i in range(len(b)):
    if not b[i].isdigit():
        b=b[:i]
        break

print(int(a) + int(b))