n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]

def is_incircle(a,b):
    return 0<=a<n and 0<=b<m

def block1(n,m):
    global max_ans
    max_ans =0
    for i in range(n):
        for j in range((m-3)+1):
            ans = 0
            for k in range(3):
                ans += arr[i][j+k]
            max_ans = max(ans,max_ans)
    for i in range(m):
        for j in range((n-3) +1):
            ans =0
            for k in range(3):
                ans += arr[j+k][i]
            max_ans =max(ans,max_ans)

def block2(n,m):
    global max_ans
    for i in range(n):
        for j in range(m):
            ans =0
            if is_incircle(i+1,j) and is_incircle(i+1,j+1) and is_incircle(i,j):
                ans += arr[i+1][j] + arr[i+1][j+1] + arr[i][j]
                max_ans = max(ans,max_ans)
    for i in range(n):
        for j in range(m):
            ans = 0
            if is_incircle(i,j) and is_incircle(i,j+1) and is_incircle(i+1,j):
                ans += arr[i][j] + arr[i][j+1] + arr[i+1][j]
                max_ans = max(ans,max_ans)     
    for i in range(n):
        for j in range(m):
            ans =0
            if is_incircle(i,j) and is_incircle(i,j+1) and is_incircle(i+1,j+1):
                ans += arr[i][j] + arr[i][j+1] + arr[i+1][j+1]
                max_ans = max(ans,max_ans)
    for i in range(n):
        for j in range(m):
            ans = 0
            if is_incircle(i,j) and is_incircle(i+1,j) and is_incircle(i+1,j-1):
                ans += arr[i][j] + arr[i+1][j] + arr[i+1][j-1]
                max_ans = max(ans,max_ans)

block1(n,m)
block2(n,m)
print(max_ans)