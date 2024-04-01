import sys
n,a,b = map(int,input().split())
arr= input()
arr = list(arr)
#print(len(arr))
max_cnt = 0
left = 0

global cnt_a
global cnt_b

def check(a,b,cnt_a,cnt_b):
    return cnt_a <= a and cnt_b>=b

def count_alpha(tmp):
    cnt_a,cnt_b = 0,0
    for i in range(len(tmp)):
        if tmp[i] =='a':
            cnt_a +=1
        else:
            cnt_b +=1
        if cnt_a > a and cnt_b >= b:
            tmp = tmp[:i]
            return tmp
    if cnt_b < b:
        tmp =[]
    return tmp

for left in range(0,n):
    tmp = arr[left:len(arr)]
    tmp = count_alpha(tmp)
    max_cnt = max(max_cnt,len(tmp))

print(max_cnt)