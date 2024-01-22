a,b = map(int,input().split())
c,d = map(int,input().split())

def is_overlap(a,b,c,d):
    if b<c or d<a: #겹치지 않았음
        return False
    return True #겹쳤음

if is_overlap(a,b,c,d):
    if d < b:
        print (abs(b-c))
    else:
        print(d-a)
else:
    print((b-a) + (d-c))