n=int(input())
arr = list(map(int,input().split()))
arr.sort()
max_num = 0
while arr:
    a = arr.pop(0)
    b = arr.pop(-1)
    if max_num < a+b:
        max_num = a+b
print(max_num)