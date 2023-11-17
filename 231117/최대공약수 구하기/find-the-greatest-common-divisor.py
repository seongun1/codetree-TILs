n,m =map(int,input().split())
def gcd (a,b):
    min_val =min(a,b)
    index = 0
    for i in range(min_val,0,-1):
        if not a%i and not b%i:
            index = i
            break
    return index

print (gcd(n,m))