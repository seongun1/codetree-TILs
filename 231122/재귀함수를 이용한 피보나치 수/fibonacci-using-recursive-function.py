n=int(input())
def fibinacchi(n):
    if n ==1:
        return 1
    elif n ==2:
        return 1
    return fibinacchi(n-2) + fibinacchi(n-1)
print(fibinacchi(n))