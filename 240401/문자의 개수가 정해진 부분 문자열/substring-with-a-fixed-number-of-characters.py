import sys
n,a,b = map(int,input().split())
arr= input()
arr = list(arr)
#print(len(arr))
max_cnt = 0
left = 0

cnt_a,cnt_b = 0,0

def check(a,b,cnt_a,cnt_b):
    return cnt_a <= a and cnt_b>=b

for left in range(0,n):
    for right in range(n,0,-1):
        tmp = arr[left:right]
        #print(tmp)
        for t in tmp:
            if t == 'a':
                cnt_a +=1
            else:
                cnt_b+=1
        if check(a,b,cnt_a,cnt_b):
            max_cnt = max(len(tmp),max_cnt)
            #print(tmp)
            cnt_a,cnt_b = 0,0 
            break
        elif cnt_b < b:
            cnt_a,cnt_b = 0,0 
            break
        cnt_a,cnt_b = 0,0 

print(max_cnt)