n=input()
n=list(n)
val =0
for i in range(len(n)):
    n[i] = int(n[i])
    val = val*2 + n[i]
val *= 17
arr=[]
while (1):
    if val <2:
        arr.append(val)
        break
    arr.append(val%2)
    val //= 2
for a in arr[::-1]:
    print(a,end='')