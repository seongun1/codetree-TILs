n,l = map(int,input().split())
arr=list(map(int,input().split()))


def is_possible(num,l):
    cnt =0
    chance_point = l
    for i in range(n):
        if arr[i] >= num:
            cnt +=1
        elif arr[i] +1 >= num and chance_point:
            cnt +=1
            chance_point -=1
    if cnt >= num:
        return True
    return False
    
max_ans =0

for i in range(1,max(arr)):
    if is_possible(i,l):
        max_ans = max(i,max_ans)
print(max_ans)