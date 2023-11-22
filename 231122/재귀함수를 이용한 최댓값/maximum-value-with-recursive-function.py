n=int(input())
arr=list(map(int,input().split()))
max_val = arr[0]
def find_max(k):
    if k==0:
        return arr[0]
    return max(find_max(k-1),arr[k])
print(find_max(n-1))