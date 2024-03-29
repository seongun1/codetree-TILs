from sys import stdin

arr =stdin.readline()

arr=list(arr)
flag = False
ans = 0

def is_correct():
    cnt =0
    stack = arr.copy()
    cnt_a,cnt_b = 0,0

    for tmp in range(len(stack)-1,-1,-1):
        if stack[tmp] =='(':
            cnt_a +=1
            cnt -=1
        else:
            cnt_b +=1
            cnt +=1
        if cnt <0:
            return False
    if cnt_a != cnt_b:
        return False
    return True

for i in range(len(arr)):
    if arr[i] == '(':
        arr[i] = ')'
    else: #a == ')'
        arr[i]='('
    #print(arr)
    if is_correct():
        #print(i)
        ans +=1
    if arr[i] == '(':
        arr[i] = ')'
    else:
        arr[i] = '('
print(ans)