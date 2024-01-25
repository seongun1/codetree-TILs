a,b,x,y = map(int,input().split())

dist = 0
if abs(b - a) > abs(a-x) or b-a > abs(a-y):
    if abs(a-x) > abs(a-y):
        dist += abs(a-y)
        dist += abs(b-x)
    else:
        dist += abs(a-x)
        dist += abs(b-y)
else:
    dist += abs(b-a)
print(dist)