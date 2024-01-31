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

# 짝수
    if group % 2 == 0:
        
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
# 홀수 
    else:

        if o > 0:
            o -= 1
            group += 1

        # elif e > 0:
        #     # 홀수를 만들때는 ( 다수의 짝수 ) + 홀수 = 홀수가 되니까 이렇게 된다.
        #     group -= 1
        else:
            break

print(group)