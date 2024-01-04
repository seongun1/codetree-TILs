n,k =map(int,input().split())
#각 사탕의 개수, 바구니의 좌표
arr=[0] * 101
for _ in range(n):
    a,b = map(int,input().split())
    arr[b] += a
ans =0
for i in range(k,100-k+1):
    tmp=0
    for j in range(i-k,i+k+1):
        tmp += arr[j]
    ans = max(ans,tmp)
print(ans)