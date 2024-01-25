a,b,x,y = map(int,input().split())

dist = 0
if abs(b - a) > abs(a-x) + abs(b-y) or abs(b-a) > abs(a-y) + abs(b-x):
    if abs(a-x) > abs(a-y):
        dist += abs(a-y) + abs(b-x)
    else:
        dist += abs(a-x) +abs(b-y)
else:
    dist += abs(b-a)
print(dist)