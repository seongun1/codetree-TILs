x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

c1 = max(x1,x2,a1,a2)
c2 = max(y1,y2,b1,b2)
d1 = min(x1,x2,a1,a2)
d2 = min(y1,y2,b1,b2)
#print(c1,c2,d1,d2)
width = c1 - d1
heigh = c2 - d2
ans = max(width,heigh)
print(ans **2)