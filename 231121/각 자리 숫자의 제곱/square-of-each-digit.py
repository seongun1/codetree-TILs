n=int(input())
def sum_val(n):
    if n<10:
        return n*n
    return sum_val(n//10) + (n%10) *(n%10)
print(sum_val(n))