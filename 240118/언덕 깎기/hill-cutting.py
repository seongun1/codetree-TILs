import sys
n=int(input())
arr=[int(input()) for _ in range(n)]
ans = sys.maxsize
for i in range(n):
    money = 0
    for j in range(n):
        if arr[j] <i:
            money += (arr[j] - i) **2
        if arr[j] > i+17:
            money += (arr[j] - i -17) **2
    ans = min(ans,money)
print(ans)