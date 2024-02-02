s = input()
t = input()

n,m = len(s), len(t)

d = [
    [n+m for _ in range(m+1)]
    for _ in range(n+1)
]

def init():
    for i in range(1,n+1):
        d[i][0] = i
        
    for i in range(1,m+1):
        d[0][i] = i

init()

for i in range(1,n+1):
    for j in range(1,m+1):
        #print("s[i] : {}, t[j] : {}".format(s[i-1], t[j-1]))
        if s[i-1] == t[j-1]:
            d[i][j] = d[i-1][j-1] - 1
            #print("d[i][j] : {}, d[i-1][j-1] : {}".format(d[i][j],d[i-1][j-1]))
        # else:
        #     d[i][j] = max(d[i-1][j], d[i][j-1])
#print(d)
print(d[n][m])