from sys import stdin
n = int(stdin.readline())
base=[[] for _ in range(n)]
for i in range(n):
    base[i] = list(map(int, stdin.readline().split()))

def check():
    xys = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    for i in range(0, 11):
        for j in range(0, 11):
            for k in range(0, 11): #축 3개의 값
                for xy1, xy2, xy3 in xys: #각 축이 x인지 y인지
                    stoppoint = True
                    for point in base:
                        if point[xy1] == i or point[xy2] == j or point[xy3] == k:
                            continue
                        stoppoint = False
                    if stoppoint:
                        return 1
    return 0
print(check())