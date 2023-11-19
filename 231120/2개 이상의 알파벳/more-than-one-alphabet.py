a=input()
def is_over_two(a):
    tmp = a[0]
    if len(a) == 1:
        return 'No'
    else:
        for i in a:
            if  tmp != i:
                return 'Yes'
        return 'No'
print(is_over_two(a))