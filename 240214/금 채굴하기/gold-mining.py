import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def getCost(k):
    return k ** 2 + (k+1) ** 2

def getGold(x,y):
    max_gold = 0
    for k in range(2 * (n-1) + 1):
        tmp = 0
        for i in range(n):
            for j in range(n):
                if abs(x-i) + abs(y-j) <= k:
                    tmp += arr[i][j]

        if tmp * m >= getCost(k):
            max_gold = max(max_gold, tmp)
                
    return max_gold

max_val = 0

for x in range(n):
    for y in range(n):
        max_val = max(max_val, getGold(x,y))

print(max_val)