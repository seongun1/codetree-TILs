a,b,c = map(int,input().split())
target =0
a,b = min(a,b),max(a,b)
cnt_b = 0
while (1):
    if target +b <= c:
        cnt_b +=1
        target +=b
    else:
        break
max_target=0
target =0

for i in range(cnt_b,-1,-1):
    target = b*i
    while (1):
        if target +a <=c:
            target +=a
        else:
            break
    max_target = max(target,max_target)
print(max_target)