s = input()
t = input()

n,m = len(s), len(t)

d = [
    [n+m for _ in range(m+1)]
    for _ in range(n+1)
]

# def init():
#     d[0][0] = m * n
#     for i in range(1,n+1):
#         d[i][0] = 
        
#     for i in range(1,m+1):
#         d[0][i] = i

# init()

#print(d)
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            d[i][j] = d[i-1][j-1] - 1
        # else:
        #     d[i][j] = max(d[i-1][j], d[i][j-1])


#print(d)
ans  = n + m
for i in range(1,n+1):
    for j in range(1,m+1):
        if d[i][j] < ans:
            ans = d[i][j]
print(ans)