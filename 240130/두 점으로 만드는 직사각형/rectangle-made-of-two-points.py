x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

s1 = min(x1,x2,a1,a2)
s2 = min(y1,y2,b1,b2)
s3 = max(x1,x2,a1,a2)
s4 = max(y1,y2,b1,b2)
#print(s1,s2,s3,s4)
print((s3 - s1) * (s4 -s2))