n,a,b = map(int,input().split())
arr= input()
arr = list(arr)
max_cnt = 0
index = 0
cnt_a,cnt_b = 0,0
while (index <=n-1):
    for right in range(n,-1,-1):
        tmp = arr[index:right]
        for t in tmp:
            if t == 'a':
                cnt_a +=1
            else:
                cnt_b+=1
        if (cnt_a <=a and cnt_b >= b and max_cnt < len(tmp)):
            max_cnt = len(tmp)
        cnt_a,cnt_b = 0,0 
    index +=1

print(max_cnt)