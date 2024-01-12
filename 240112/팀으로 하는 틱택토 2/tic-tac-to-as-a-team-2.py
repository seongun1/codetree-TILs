arr=[]
for _ in range(3):
    tmp = str(input())
    arr.append(list(tmp))
cnt =0
for i in range(3):
    if (arr[i][0] == arr[i][1] and arr[i][0] != arr[i][2]) or (arr[i][0] == arr[i][2] and arr[i][0] != arr[i][1]) or (arr[i][1] == arr[i][2] and arr[i][1] != arr[i][0]):
        cnt +=1
for j in range(3):
    if (arr[0][j] == arr[1][j] and arr[0][j] != arr[2][j]) or (arr[0][j] == arr[2][j] and arr[0][j] != arr[1][j]) or (arr[1][j] == arr[2][j] and arr[1][j] != arr[0][j]):
        cnt +=1

if (arr[0][0] == arr[1][1] and arr[0][0] != arr[2][2]) or (arr[0][0] == arr[2][2] and arr[0][0] != arr[1][1]) or (arr[1][1] == arr[2][2] and arr[1][1] != arr[0][0]):
    cnt +=1
if (arr[0][2] == arr[1][1] and arr[0][2] != arr[2][0]) or (arr[0][2] == arr[2][0] and arr[0][2] != arr[1][1]) or (arr[1][1] == arr[2][0] and arr[2][0] != arr[0][2]):
    cnt +=1
print(cnt)