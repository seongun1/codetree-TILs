n = int(input())

line = []
for i in range(n):
    s,e = map(int,input().split())
    line.append([s,e])

line.sort(key=lambda x:x[1])

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if line[i][1] < line[j][0]:
            cnt += 1
            break
print(cnt+1)