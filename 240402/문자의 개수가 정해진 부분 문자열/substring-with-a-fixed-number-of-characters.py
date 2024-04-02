from sys import stdin
# input = stdin.readline()
n,a,b = map(int,stdin.readline().split())
arr= stdin.readline()
arr = list(arr)
#print(len(arr))
max_cnt = 0

def count_alpha(tmp,a,b):
    cnt_a,cnt_b = 0,0
    for i in range(len(tmp)):
        if tmp[i] =='a':
            cnt_a +=1
        else:
            cnt_b +=1
        if cnt_a > a and cnt_b >= b:
            return tmp[:i]
    if cnt_b < b:
        tmp =[]
    return tmp

for left in range(0,n):
    tmp = arr[left:len(arr)]
    tmp = count_alpha(tmp,a,b)
    max_cnt = max(max_cnt,len(tmp))
    
print(max_cnt)