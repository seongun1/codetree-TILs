n=int(input())
def print_num1(n):
    if n==0:
        return
    print_num1(n-1)
    print(n,end=' ')

def print_num2(n):
    if n==0:
        return
    print(n,end=' ')
    print_num2(n-1)
print_num1(n)
print()
print_num2(n)