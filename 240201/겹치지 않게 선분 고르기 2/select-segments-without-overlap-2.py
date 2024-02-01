n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

arr.sort()

d = [1] * n

for i in range(1,n):
    for j in range(i):
        i_x1, _ = arr[i]
        _, j_x2 = arr[j]

        if j_x2 < i_x1:
            d[i] = max(d[i], d[j] + 1)

print(max(d))