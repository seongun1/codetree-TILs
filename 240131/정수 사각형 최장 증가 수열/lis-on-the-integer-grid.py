n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

d = [
    [1 for _ in range(n)]
    for _ in range(n)
]

cells = []
for i in range(n):
    for j in range(n):
        cells.append((arr[i][j], i, j))

# 정수값이 큰 쪽으로 이동 -> 작은 값부터 for loop를 채워야 한다
cells.sort()

max_val = 0
for _,x,y in cells:

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if in_range(next_x, next_y) and arr[next_x][next_y] > arr[x][y]:
            d[next_x][next_y] = max(d[next_x][next_y], d[x][y] + 1)

for i in range(n):
    for j in range(n):
        max_val = max(max_val, d[i][j])
print(max_val)