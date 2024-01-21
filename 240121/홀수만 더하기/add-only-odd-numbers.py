n=int(input())
arr=[int(input()) for _ in range(n)]
ans =0
for a in arr:
    if not a%3 and a%2:
        ans +=a
print(ans)