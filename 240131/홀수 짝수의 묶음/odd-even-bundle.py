n = int(input())
arr = list(map(int,input().split()))

e,o = 0,0
for i in arr:
    if i % 2 == 0:
        e += 1
    else:
        o += 1

group = 0
while True:

    if group % 2 == 0:
        # 짝수
        if e > 0:
            e -= 1
            group += 1
        elif o >= 2:
            o -= 2
            group += 1
        else:
            if o > 0:
                group -= 1
            break
    else:
        if o > 0:
            o -= 1
            group += 1
        else:
            if e > 0:
                group -= 1
            break
print(group)