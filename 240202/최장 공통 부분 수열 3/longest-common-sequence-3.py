n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열을 뒤집습니다.
a.reverse()
b.reverse()

a = [0] + a
b = [0] + b

INF = 1987654321

dp = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

path =[
    [(0,0) for _ in range(m+1)]
    for _ in range(n+1)
]

cur_best = [
    [INF] * (m + 1) 
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 각 단계에서 최적의 해를 찾습니다.
        if dp[i - 1][j] > dp[i][j] or (dp[i - 1][j] == dp[i][j] and cur_best[i - 1][j] < cur_best[i][j]):
            dp[i][j] = dp[i - 1][j]
            path[i][j] = (i - 1, j)
            cur_best[i][j] = cur_best[i - 1][j]
        
        if dp[i][j - 1] > dp[i][j] or (dp[i][j - 1] == dp[i][j] and cur_best[i][j - 1] < cur_best[i][j]):
            dp[i][j] = dp[i][j - 1]
            path[i][j] = (i, j - 1)
            cur_best[i][j] = cur_best[i][j - 1]

        if a[i] == b[j] and (dp[i - 1][j - 1] + 1 > dp[i][j] or (dp[i - 1][j - 1] + 1 == dp[i][j] and a[i] < cur_best[i][j])):
            dp[i][j] = dp[i - 1][j - 1] + 1
            path[i][j] = (i - 1, j - 1)
            cur_best[i][j] = a[i]

lcs = []
i, j = n, m
while i > 0 and j > 0:
    if path[i][j] == (i - 1, j - 1) and a[i] == b[j]:
        lcs.append(a[i])
        i -= 1
        j -= 1
    else:
        i, j = path[i][j]

print(' '.join(map(str, lcs)))