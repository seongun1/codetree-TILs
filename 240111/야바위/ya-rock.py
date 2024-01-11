n=int(input())
arr=[0]*4
max_cnt=0
tmp = [list(map(int,input().split()))for _ in range(n)]
for i in range(1,4):
    arr[i] = 1
    cnt=0
    for t in range(n):
        arr[tmp[t][0]],arr[tmp[t][1]] = arr[tmp[t][1]],arr[tmp[t][0]]
        if arr[tmp[t][2]] == 1:
            cnt +=1
    arr=[0] *4
    max_cnt = max(max_cnt,cnt)
print(max_cnt)