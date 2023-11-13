arr= [[0 for i in range(5)] for _ in range(5)]
for i in range(5):
    arr[0][i] = 1
for i in range(5):
    arr[i][0] = 1
for i in range(4):
    for j in range(4):
        arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j]
for a in arr:
    for i in a:
        print(i,end=' ')
    print()