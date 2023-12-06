# 8방향중 쭉 이동 가능한데, 자신의 값보다 큰 값으로 이동을 최대한 많이 이동
import sys
sys.setrecursionlimit(10**7)

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

direction = []
for i in range(n):
    direction.append(list(map(int,input().split())))

r,c = map(int,input().split())
r -= 1
c -= 1
move, max_val = 0, 0
cur_x, cur_y = -1,-1

def find_max_val_by_direct(x,y):
    global max_val, cur_x, cur_y
    direct = direction[x][y]
    # 홀수가 북 동 남 서
    if direct == 1:
        for r in range(x+1):
            cur_x, cur_y = r,y
            max_val = max(arr[r][y], max_val)
    elif direct == 3:
        for c in range(y,n):
            cur_x, cur_y = x,c
            max_val = max(arr[x][c], max_val)
    elif direct == 5:
        for r in range(x,n):
            cur_x, cur_y = r,y
            max_val = max(arr[r][y], max_val)
    elif direct == 7:
        for c in range(y+1):
            cur_x, cur_y = x,c
            max_val = max(arr[x][c], max_val)

    # 짝수가 북동 남동 남서 북서
    elif direct == 2:
        for i in range(n):
            if (x - i == -1) or (y + i == n):
                break
            cur_x, cur_y = x-i,y+i
            max_val = max(arr[x-i][y+i], max_val)
    elif direct == 4:
        for i in range(n):
            if (x + i == n) or (y + i == n):
                break
            cur_x, cur_y = x+i,y+i
            max_val = max(arr[x+i][y+i], max_val)
    elif direct == 6:
        for i in range(n):
            if (x + i == n) or (y - i == -1):
                break
            cur_x, cur_y = x+i,y-i
            max_val = max(arr[x+i][y-i], max_val)
    elif direct == 8:
        for i in range(n):
            if (x - i == -1) or (y - i == -1):
                break
            cur_x, cur_y = x-i,y-i
            max_val = max(arr[x-i][y-i], max_val)
    

def choose(x,y):
    global move, max_val, cur_x, cur_y

    find_max_val_by_direct(x,y)


    # 해당 방향에 더이상 높은 값이 없다 
    if arr[x][y] == max_val:
        return move
    
    # 이동할 수 있으면 이동
    choose(cur_x,cur_y)
    move += 1

choose(r,c)
print(move)