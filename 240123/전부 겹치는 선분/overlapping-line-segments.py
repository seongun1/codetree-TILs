n=int(input())
arr= [list(map(int,input().split())) for _ in range(n)]
arr_list = [0] * 101
for a in arr:
    x1,x2 = a
    for i in range(x1,x2+1):
        arr_list[i] +=1
def is_correct(n):
    for a in arr_list:
        if a == n:
            return "Yes"
    return "No"

print(is_correct(n))