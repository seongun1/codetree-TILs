T = int(input())  # 테스트 케이스 수
mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

grid = [
    [-1 for _ in range(4001)]
    for _ in range(4001)
]

def in_range(i, j):
    return 0 <= i < 4001 and 0 <= j < 4001

for _ in range(T):
    arr = []
    N = int(input())  # 구슬 개수
    for num in range(1, N+1):
        x, y, w, d = input().split()
        i, j, w, dNum = (-int(y)) * 2 + 2000, int(x) * 2 + 2000, int(w), mapper[d]

        arr.append((num, i, j, w, dNum))

    record = -1

    for t in range(1, 4001):
        next_arr = []
        # 이동
        for i in arr:
            num, x, y, w, d = i
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny):
                if grid[nx][ny] == -1:
                    next_arr.append((num, nx, ny, w, d))
                    grid[nx][ny] = len(next_arr) - 1
                else:
                    record = t
                    # 무게가 크면
                    if next_arr[grid[nx][ny]][3] < w:
                        next_arr[grid[nx][ny]] = (num, nx, ny, w, d)
                    # 무게가 같고 번호가 크면
                    elif next_arr[grid[nx][ny]][3] == w and next_arr[grid[nx][ny]][0] < num:
                        next_arr[grid[nx][ny]] = (num, nx, ny, w, d)

        arr = next_arr[:]

        #다음 수행을 위한 초기화
        for i in next_arr:
            grid[i[1]][i[2]] = -1

    print(record)