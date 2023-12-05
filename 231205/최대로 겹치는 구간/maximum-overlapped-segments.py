n=int(input())
arr= [0 for _ in range(200)]
for i in range(n):
    a,b = map(int,input().split())
    a,b= a+100,b+100
    for j in range(a,b):
        arr[j] +=1
print(max(arr))