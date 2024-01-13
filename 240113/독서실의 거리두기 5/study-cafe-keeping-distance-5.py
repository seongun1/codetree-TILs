from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()

ans = 0
for i in range(n): #위치 선정
    if base[i] == '1': #사용자 있음
        continue
    tmp = float("inf")
    
    indices = [
        j for j in range(n)
        if base[j] == '1' or i == j
    ]

    m = len(indices)

    for i in range(m - 1):
        tmp = min(tmp, indices[i + 1] - indices[i])

    ans = max(ans, tmp)
print(ans)