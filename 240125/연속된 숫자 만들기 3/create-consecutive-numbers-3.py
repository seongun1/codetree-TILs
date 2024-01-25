a,b,c = map(int,input().split())
cnt =0
while (1):
    if abs(a-b) ==1 and abs(b-c) ==1:
        break
    cnt +=1
    if abs(a-b) >= abs(b-c):
        c = b-1
        a,b,c = a,c,b
    else:
        a = c-1
        a,b,c = b,a,c

print(cnt)