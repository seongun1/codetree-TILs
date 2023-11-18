n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

endPoint = -1 
cnt = 0  

for i in arr:
    start, end = i
    if start > endPoint:
        cnt += 1
        endPoint = end

print(cnt)