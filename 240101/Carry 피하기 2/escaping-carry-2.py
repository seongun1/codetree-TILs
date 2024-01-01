n=int(input())
arr =[int(input()) for _ in range(n)]
max_ans =0
ans=-1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i] //1000 + arr[j]//1000 + arr[k]//1000 <10 and arr[i]//100%10 + arr[j]//100%10 + arr[k]//100%10 < 10 and arr[i] //10%10 + arr[j]//10%10 + arr[k]//10%10 < 10 and arr[i] %10 + arr[j] %10 + arr[k] %10 <10:
                ans = arr[i]+arr[j]+arr[k]
                break
        max_ans = max(ans,max_ans)

print(max_ans)