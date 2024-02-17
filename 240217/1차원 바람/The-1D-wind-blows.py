from collections import deque
n,m,q = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

wind = list()

for _ in range(q):
    row, direct = input().split()
    row = int(row) - 1
    wind.append((row, direct))

def move(tmp_arr, row, direct):
    q = deque(tmp_arr)

    if direct == 'L': # 오른쪽으로 이동
        data = q.pop()
        q.appendleft(data)
        # tmp = tmp_arr[-1]

        # for i in range(m-2,-1,-1):
        #     tmp_arr[i+1] = tmp_arr[i]
        # tmp_arr[0] = tmp

    elif direct == 'R':
        data = q.popleft()
        q.append(data)
        
        # tmp = tmp_arr[0]

        # for i in range(1,m):
        #     tmp_arr[i-1] = tmp_arr[i]
        # tmp_arr[-1] = tmp

    return q

def checkArr(arr1, arr2):
    for i in range(m):
        if arr1[i] == arr2[i]:
            return True
    return False

for i in wind:
    row, direct = i

    up_direct, down_direct = list(), list()

    if direct == 'L':
        up_direct.append(0)
        down_direct.append(0)
    else:
        up_direct.append(1)
        down_direct.append(1)

    arr[row] = move(arr[row], row , direct)
    
    for i in range(row,0,-1):
        if checkArr(arr[i], arr[i-1]):

            if up_direct[-1] == 1:
                arr[i-1] = move(arr[i-1], i-1 , 'L')
                up_direct.append(0)
                continue

            else:
                arr[i-1] = move(arr[i-1], i-1 , 'R')
                up_direct.append(1)
                continue

    for i in range(row,n-1):
        if checkArr(arr[i], arr[i+1]):

            if up_direct[-1] == 1:
                arr[i+1] = move(arr[i+1], i+1 , 'L')
                up_direct.append(0)
                continue

            else:
                arr[i+1] = move(arr[i+1], i+1 , 'R')
                up_direct.append(1)
                continue
                
for i in arr:
    print(*i)