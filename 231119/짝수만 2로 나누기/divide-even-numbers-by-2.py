n=int(input())
arr= list(map(int,input().split()))
def div_even(arr):
    for a in arr:
        if not a%2:
            a /=2
        print (int(a),end=' ')
div_even(arr[:])