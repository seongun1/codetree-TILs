import sys

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def checkLine(tmp):
    for i in range(n - m + 1):
        flag = True

        for j in range(i, i + m):
            if tmp[i] != tmp[j]:
                flag = False
                break
        
        if flag:
            return True

    return False

cnt = 0
for x in range(n):
    row_arr, col_arr = [], []
    for y in range(n):
        row_arr.append(arr[x][y])
    
    for y in range(n):
        col_arr.append(arr[y][x])

    if checkLine(row_arr):
        cnt += 1

    if checkLine(col_arr):
        cnt += 1
print(cnt)