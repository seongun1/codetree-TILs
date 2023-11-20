n,m = map(int,input().split())
arr=list(map(int,input().split()))

def is_even(a):
    a /=2
    return int(a)
def is_odd(a):
    a -=1
    return int(a)
ans =0
while (1):
    ans += arr[m-1]
    if not m %2:
        m = is_even(m)
    else:
        m= is_odd(m)
    if m ==1:
        break
ans += arr[m-1]
print(ans)