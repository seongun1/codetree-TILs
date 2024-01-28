from sys import stdin
n = 10
base = []
for _ in range(n):
    base.append(stdin.readline().strip())

for i in range(n):
    for j in range(n):
        if base[i][j] != ".":
            if base[i][j] == "B":
                B=[i, j]
            elif base[i][j] == "R":
                R=[i, j]
            elif base[i][j] == "L":
                L=[i, j]

#L, B가 일직선이 최단 경로일때 거기에 R이 있을대만 경로가 2개 증가

ans = abs(B[0]-L[0])+abs(B[1]-L[1])-1
if min(B[0],L[0])<R[0]<max(B[0],L[0]) and B[1]==L[1]==R[1]:
    ans += 2
elif min(B[1],L[1])<R[1]<max(B[1],L[1]) and B[0]==L[0]==R[0]:
    ans += 2
print(ans)