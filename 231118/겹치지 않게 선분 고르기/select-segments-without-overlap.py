n = int(input())
line = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    line.append((x1, x2))

line.sort(key=lambda x: x[0])

end = line[0][1]  
count = 1  

for i in range(1, n):
    start, finish = line[i] 

    if start >= end:
        count += 1
        end = finish

print(count)