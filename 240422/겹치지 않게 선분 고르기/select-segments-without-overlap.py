n = int(input())

line = []
for i in range(n):
    s,e = map(int,input().split())
    line.append([s,e])

line.sort(key=lambda x:x[1])

cnt = 1
idx = line[0][1]

for i in range(1,n):
    if idx < line[i][0]:
        cnt += 1
        idx = line[i][1]

print(cnt)