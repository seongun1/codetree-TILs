import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs, dys = [-1,1,0,0], [0,0,-1,1]

def getCost(k):
    return k ** 2 + (k+1) ** 2

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def getGold(x,y):
    max_gold = -sys.maxsize
    for k in range(n):
        tmp = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j]:
                    tmp += 1

                if abs(x-i) + abs(y-j) == k:
                    max_gold = max(max_gold, tmp - getCost(k))
    return max_gold

max_val = -sys.maxsize

for x in range(n):
    for y in range(n):
        max_val = max(max_val, getGold(x,y))

print(max_val)