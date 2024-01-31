n=int(input())
arr= [list(map(int,input().split())) for _ in range(n)]
import sys

ans =sys.maxsize
for i in range(n):
    min_a,max_b = sys.maxsize,-sys.maxsize
    for j in range(n):
        if i==j:
            continue
        a,b = arr[j]
        min_a,max_b = min(a,min_a),max(b,max_b)
    ans = min(max_b -min_a,ans)
print(ans)