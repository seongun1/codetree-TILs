n,m =map(int,input().split())
def gcd (a,b):
    min_val =0
    index = 0
    if a<b:
        min_val = a
    else:
        min_val =b
    for i in range(min_val,0,-1):
        if not a%i and not b%i:
            index = i
            break
    return index

print (gcd(n,m))