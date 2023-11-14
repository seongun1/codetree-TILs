n,m,t = map(int,input().split())

arr = [[[] for _ in range(n)]for _ in range(n)]
next_arr = [[[] for _ in range(n)]for _ in range(n)]

mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

dx, dy = [-1,0,0,1], [0,1,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(1,m+1):
    r,c,d,w = input().split()

    arr[int(r)-1][int(c)-1] = [(i, int(w), mapper[d])] # 번호 , 무게 , 방향

# print('---초기 arr----')
# for i in arr:
#     print(*i)
# print('-------')

def next_pos(x,y,direct):
    
    nx ,ny = x + dx[direct], y + dy[direct]

    if not in_range(nx,ny):
        direct = 3 - direct
        return (x,y,direct)
    else:
        return (nx,ny,direct)
    

def move_all():
    for x in range(n):
        for y in range(n):
            for idx, w, direct in arr[x][y]:
                next_x,next_y,next_dir = next_pos(x,y,direct)
                next_arr[next_x][next_y].append((idx, w, next_dir))

max_weight = -1
max_num = m

def simulate():
    global max_num
    for i in range(n):
        for j in range(n): # 구슬 번호, 구슬 무게, 방향
            length = len(next_arr[i][j])
            if length == 0:
                continue

            if length >= 2:
                w = 0
                temp_num, new_dir = -1 , next_arr[i][j][0][2]
                
                for h in range(length):
                    w += next_arr[i][j][h][1]

                    if next_arr[i][j][h][0] >= temp_num:
                        temp_num = next_arr[i][j][h][0]
                        new_dir = next_arr[i][j][h][2]
                        
                max_num += 1
                next_arr[i][j] = [(max_num, w, new_dir)]



for _ in range(t):
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = []
		
    move_all()
    simulate()

    # print('-----중간 점검-----')
    # for i in next_arr:
    #     print(*i)
    # print('----------')
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != []:
            if arr[i][j][0][1] >= max_weight:
                max_weight = arr[i][j][0][1]
            cnt += 1

print(cnt, max_weight)