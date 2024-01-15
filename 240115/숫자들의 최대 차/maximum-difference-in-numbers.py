n,k = map(int,input().split())
arr=[int(input()) for _ in range(n)]
ans =[]
for a in arr:
    if len(ans) ==0:
        ans.append(a)
    elif min(ans) <= a <= max(ans):
        ans.append(a)
    elif a < min(ans):
        if  max(ans)-a <=3:
            ans.append(a)
    elif a > max(ans):
        if a - min(ans) <= 3:
            ans.append(a)
print(len(ans))