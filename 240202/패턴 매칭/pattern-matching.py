import sys
input = sys.stdin.readline()

s = input
p = input

n = len(s)
m = len(p)

d = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

def init():
    d[0][0] = 0

    for i in range(1,n+1):
        d[i][0] = i
    for i in range(1,m+1):
        d[0][i] = i

init()

for i in range(1,n+1):
    flag = False
    for j in range(1,m+1):
        if s[i-1] == p[j-1]:
            break
        if '*' == p[j-1]:
            sys.exit(0)
        if '.' == p[j-1]:
            break
        else:
            flag = True
            break
    if flag:
        break
    
if flag:
    print("false")
else:
    print("true")