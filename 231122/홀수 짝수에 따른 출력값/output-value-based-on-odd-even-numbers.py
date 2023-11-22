n=int(input())

def print_val(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return  print_val(n-2) +n

print(print_val(n))