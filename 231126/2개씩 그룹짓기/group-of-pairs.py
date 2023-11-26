n=int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[0] + arr[-1] if arr[0]+ arr[-1] >= arr[n-1] + arr[n] else arr[n-1] + arr[n])