n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
ans =1

def find_num(a,b,num):
    if a<=num<=b:
        return True
    return False

ans =1
while(1):
    flag = True
    tmp = ans
    tmp *=2
    for a,b in arr:
        if not find_num(a,b,tmp):
            ans +=1
            flag =False
            break
        else:
            tmp *=2
    if flag:
        break
print(ans)