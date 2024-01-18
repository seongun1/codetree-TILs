arr = list(map(int,input().split()))
n = len(arr)
arr.sort()
def possible():
    for q in range(n):
        for w in range(n):
            for e in range(n):
                for r in range(n):
                    if q!=w and w!=e and e!=r and q!=r and q!=e and w!=r:
                        a,b,c,d = arr[q],arr[w],arr[e],arr[r]
                        if (a+b in arr) and (b+c in arr) and (c+d in arr) and (d+a in arr) and (a+c in arr) and (b+d in arr) and (a+b+c in arr) and (a+b+d in arr) and (a+c+d in arr) and (b+c+d in arr) and  (a+b+c+d in arr):
                            print(a,b,c,d)
                            return
    return False

possible()