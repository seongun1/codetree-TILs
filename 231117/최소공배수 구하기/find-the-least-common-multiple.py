n,m = map(int,input().split())
def find_cheso(a,b):
    i = max(a,b)
    index =0
    while (1):
        if not i%a and not i%b:
            index = i
            break
        i +=1
    return index
print(find_cheso(n,m))