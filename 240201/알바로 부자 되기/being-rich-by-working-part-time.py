n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

d = [0] * n
for i in range(n):
    d[i] = arr[i][2]

for i in range(1,n):
    for j in range(i):
        
        s1, _ , _ = arr[i]
        _, e2 , p2 = arr[j]

        if e2 < s1:
            d[i] = max(d[i], d[j] + p2)

print(max(d))