n = int(input())
boom_cnt = 0 # 폭탄 개수

arr,ans = [], []
for i in range(n):
    arr.append(list(map(int,input().split())))

dx,dy = [-1,1,0,0],[0,0,-1,1]
dxs,dys = [-1,-1,1,1],[-1,1,-1,1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            boom_cnt += 1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def boom(tmp):
    idx, cnt = 0,0
    flag = False

    new_arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                if tmp[idx] == 1:
                    for h in range(-2,3):
                        if not in_range(i+h,j):
                            continue
                        new_arr[i+h][j] = -1

                elif tmp[idx] == 2:
                    new_arr[i][j] = -1
                    for h in range(4):
                        nx,ny = i + dx[h], j + dy[h]
                        if in_range(nx,ny):
                            new_arr[nx][ny] = -1

                elif tmp[idx] == 3:
                    new_arr[i][j] = -1
                    for h in range(4):
                        nx,ny = i + dxs[h], j + dys[h]
                        if in_range(nx,ny):
                            new_arr[nx][ny] = -1
                    

                idx += 1
                if idx == boom_cnt:
                    flag = True
                    break
        if flag:
            break

    for i in range(n):
        for j in range(n):
            if new_arr[i][j] == -1:
                cnt += 1
    
    for i in new_arr:
        print(*i)
    print('---')

    return cnt

maxcnt = -1
def print_ans():
    global maxcnt
    cnt = boom(ans) # [1, 1] \n [1,2]

    if cnt >= maxcnt:
        maxcnt = cnt
    

def choose(cur_num): # cur_num은 해당 자리 위치
    if cur_num == boom_cnt+1:
        print_ans()
        return
    
    for i in range(1, 4):  
        ans.append(i)
        choose(cur_num + 1)
        ans.pop()
    return

choose(1)
print(maxcnt)