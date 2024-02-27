n,m,t = map(int,input().split())

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# 상 좌 우 하
dxs, dys = [-1,0,0,1], [0,-1,1,0]

mapper = {
    'U' : 0,
    'L' : 1,
    'R' : 2,
    'D' : 3
}

for i in range(m):
    x,y,d,w = input().split()
    x,y,w = int(x), int(y), int(w)
    arr[x-1][y-1].append([w, i+1, mapper[d]]) # 구슬 무게, 번호, 방향

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(x,y,d):
    nx,ny = x + dxs[d], y + dys[d]

    if not in_range(nx,ny):
        d = 3 - d
        return x,y,d
    
    return nx,ny,d

def move_all():
    for i in range(n):
        for j in range(n):
            for w, idx, direct in arr[i][j]:
                x,y,d = move(i,j,direct)
                temp[x][y].append([w, idx, d])

def arrange():
    for i in range(n):
        for j in range(n):
            if len(temp[i][j]) == 0:
                continue
            
            weight, max_num , direction = 0, -1, 0

            for w, num, direct in temp[i][j]:
                weight += w
                if max_num <= num:
                    max_num = num
                    direction = direct
            
            temp[i][j] = [[weight, max_num, direction]]

    
for _ in range(t):
    temp = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
		
    move_all()
    arrange()
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

    
val,max_weight = 0, 0
for i in range(n):
    for j in range(n):
        if len(arr[i][j]) == 0:
            continue
        val += 1

        for vals in arr[i][j]:
            if vals[0] > max_weight:
                max_weight = vals[0]

print(val, max_weight)