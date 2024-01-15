import sys
sum_arr=list(map(int,input().split()))
sum_arr.sort()

def find_ans(a,b,c,d):
    if a+b in sum_arr and b+c in sum_arr and c+d in sum_arr and d+a in sum_arr and a+c in sum_arr and d+b in sum_arr and a+b+c in sum_arr and a+b+d in sum_arr and a+c+d in sum_arr and b+c+d in sum_arr and a+b+c+d in sum_arr:
        return True
    return False

for a in range(1,41):
    for b in range(1,41):
        for c in range(1,41):
            for d in range(1,41):
                if find_ans(a,b,c,d):
                    print(a,b,c,d)
                    sys.exit()