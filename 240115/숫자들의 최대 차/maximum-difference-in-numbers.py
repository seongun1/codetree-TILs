n,k = map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.sort()
max_ans_len = 0
for i in range(n):
    start = arr[i]
    ans =[]
    ans.append(start)
    for j in range(n):
        if i==j:
            continue
        if min(ans) <= arr[j] <= max(ans):
            ans.append(arr[j])
        elif arr[j] < min(ans) and max(ans) - arr[j] <=k :
            ans.append(arr[j])
        elif max(ans) < arr[j] and arr[j] - min(ans) <= k:
            ans.append(arr[j])
    max_ans_len = max(len(ans),max_ans_len)
print(max_ans_len)