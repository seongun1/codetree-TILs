n,k = map(int,input().split())
def print_dp(n):
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
arr=[' '] * (k+1)
def count_arr():
    arr[0] = [['0']]
    arr[1] =[['1']]
    arr[2] =[['1+1'],['2']]
    for i in range(3,n+1):
        for a in arr:
            arr[i] = a+'1'
    print(arr[3])

#dp[n] = dp[n-1] + dp[n-2] + dp[n-3]  (n>=3)
dp=[-1] * (k+1)
dp[0],dp[1],dp[2] = 0,1,2 

print_dp(n)

count_arr()