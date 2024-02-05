n = int(input())
arr=list(input().split() for _ in range(n))
d_arr=[]
for i in range(n):
    if arr[i][0]=='push_back':
        d_arr.append(int(arr[i][1]))
    elif arr[i][0] == 'pop_back':
        d_arr.pop()
    elif arr[i][0] == 'size':
        print(len(d_arr))
    elif arr[i][0] =='get':
        print(d_arr[int(arr[i][1]) -1])