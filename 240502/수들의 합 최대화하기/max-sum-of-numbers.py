import sys
n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False] * (n+1)

max_val = -sys.maxsize
ans = []

def calc():
    return sum([
        i for i in ans
    ])

def choose(cnt):
    global max_val

    if cnt == n:
        max_val = max(max_val , calc())
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i][cnt])

            choose(cnt+1)

            ans.pop()
            visited[i] = False

choose(0)
print(max_val)