n,m,k = map(int,input().split())
arr=[0] *(n+1)

def penelty():
    global ans
    ans = -1
    for _ in range(m):
        tmp = int(input())
        arr[tmp] +=1
        for i in range(1,n+1):
            if arr[i] >= k:
                ans =i
                return ans
    return ans
print(penelty())