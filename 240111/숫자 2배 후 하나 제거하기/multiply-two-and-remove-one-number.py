import sys
n=int(input())
arr=list(map(int,input().split()))
min_ans = sys.maxsize
for i in range(n):
    arr[i] *=2
    for j in range(n):
        last=[]
        for k,elem in enumerate(arr):
            if k == j:
                continue
            last.append(elem)
        cnt =0
        for p in range(n-2):
            cnt += abs(last[p+1] - last[p])
        min_ans = min(cnt,min_ans)
    arr[i] //=2
print(min_ans)