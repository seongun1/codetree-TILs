n=input()
def decision(n):
    tmp =0
    for i in n:
        tmp += int(i)
    if not int(n)%2 and not tmp%5:
        return ('Yes')
    else:
        return ('No')
print(decision(n))