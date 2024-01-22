x1,x2,x3,x4 = map(int,input().split())

def is_intersect(a,b,c,d):
    if b<c or d<a:
        return False
    return True

    
print("intersecting") if is_intersect(x1,x2,x3,x4) else print("nonintersecting")