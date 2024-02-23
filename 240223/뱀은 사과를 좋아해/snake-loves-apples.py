n,m,k = map(int,input().split())

arr = [[0] * n for _ in range(n)]

# 사과 = 2
for _ in range(m):
    x,y = map(int,input().split())
    arr[x-1][y-1] = 2


direct = []
total_cnt = 0 # 뱀이 움직이는 총 횟수
for i in range(k):
    d,length = input().split()
    total_cnt += int(length)
    direct.append([d, int(length)])

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def meet_my_body(x,y):
    if arr[x][y] == 1: # 만남
        return True
    return False


# 동 남 서 북 -> 오른쪽을 보니까 시계 방향 반시계 방향 체크 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

mapper = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3
}

x,y = 0,0

def process():
    global x, y, total_cnt
    time = 0
    arr[x][y] = 1 # 뱀 위치
    q = [(x,y)]

    if k == 0:
        return 0

    while True:

        for d,length in direct:

            if total_cnt == 0:
                return time

            for j in range(length):

                nx, ny = x + dx[mapper[d]], y + dy[mapper[d]]
                
                time += 1

                if not in_range(nx,ny):
                    return time

                if arr[nx][ny] == 2: # 사과 있음 
                    arr[nx][ny] = 1
                    q.append((nx,ny))
                
                elif arr[nx][ny] == 0 or arr[nx][ny] == 1: # 사과 없음
                    hx,hy = q.pop(0)
                    arr[hx][hy] = 0
                    if meet_my_body(nx,ny):
                        return time
                    arr[nx][ny] = 1
                    q.append((nx,ny))
                
                x,y = nx,ny
                total_cnt -= 1


ans = process()
print(ans)