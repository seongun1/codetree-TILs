n,m,c = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

a = list()
max_value = 0

def interact(a,b,c,d):
    return not (b<c or d<a)

def find_max_sum(idx, weight, val):
    global max_value

    if idx == m:
        if weight <= c:
            max_value = max(max_value, val)
        return
    
    # idx 해당 데이터 선택안함
    find_max_sum(idx+1, weight, val)
    # idx 해당 데이터 선택함
    find_max_sum(idx+1, weight + a[idx], val + a[idx] * a[idx])

def find_max(x,y):
    global a, max_value

    a = arr[x][y:y+m]

    max_value = 0
    find_max_sum(0,0,0)
    return max_value


def possible(x1,y1,x2,y2):
    if y1+m-1 >= n or y2+m-1 >= n:
        return False

    if x1 != x2:
        return True

    if interact(y1,y1+m-1,y2,y2+m-1):
        return False

    return True

ans = 0

for sx1 in range(n):
    for sy1 in range(n):
        for sx2 in range(n):
            for sy2 in range(n):
                if possible(sx1, sy1, sx2, sy2):
                    ans = max(ans, find_max(sx1, sy1) + find_max(sx2, sy2))

print(ans)