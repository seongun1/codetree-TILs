n=int(input())
a= list(map(int,input().split()))
b=list(map(int,input().split()))
def is_same():
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] != b[i]:
            return 'No'
        return 'Yes'
print(is_same())