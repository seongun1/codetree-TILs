# a = input()
# b = input()

# n = len(a)
# m = len(b)

# d = [
#     [0 for _ in range(m+1)]
#     for _ in range(n+1)
# ]

# # def init():
# #     d[0][0] = 1 if a[0] == b[0] else 0

# #     for i in range(1,n):
# #         if a[i] == b[0]:
# #             d[i][0] = 1
# #         else:
# #             d[i][0] = d[i-1][0]

# #     for j in range(1,m):
# #         if a[0] == b[j]:
# #             d[0][j] = 1
# #         else:
# #             d[0][j] = d[0][j-1]
            
# # init()
# #print(n,m)
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if a[i] == b[j]:
#             d[i][j] = d[i-1][j-1] + 1
#         else:
#             d[i][j] = max(d[i-1][j], d[i][j-1])

# #print(d)

# print(d[n][m])

s = input()
t = input()

n,m = len(s), len(t)

d = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]


for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])
print(d[n][m])