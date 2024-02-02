a = input()
b = input()

n = len(a)
m = len(b)

d = [
    [0 for _ in range(m+1)]
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
        if a[i-1] == b[j-1]:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = min(d[i-1][j], d[i][j-1]) + 1
    
print(d[n][m])