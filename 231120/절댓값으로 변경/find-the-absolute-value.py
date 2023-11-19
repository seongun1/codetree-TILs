n=int(input())
arr= list(map(int,input().split()))
def abs_num(n):
    return abs(n)
for i in arr:
    print(abs_num(i),end=' ')