n=int(input())
def print_odd(n):
    if n ==1:
        return 1
    return print_odd(n-2) + n
def print_even(n):
    if n==0:
        return 0
    return  print_even(n-2) +n
if not n%2:
    print(print_even(n))
else:
    print(print_odd(n))