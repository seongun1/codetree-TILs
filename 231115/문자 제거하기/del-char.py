a=input()
while (len(a) >1):
    a=list(a)
    tmp = int(input())
    if tmp > len(a) -1:
        a.pop(-1)
        print(''.join(a))
        continue
    a.pop(tmp)
    print(''.join(a))