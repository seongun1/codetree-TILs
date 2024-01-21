n,m = map(int,input().split())
arr= list(map(int,input().split()))

def is_possible(possible_max):
    curr_sum =0
    curr_section =1

    for i in range(n):
        if arr[i] > possible_max:
            return False
    
        if curr_sum + arr[i] > possible_max:
            curr_sum =0
            curr_section +=1
        curr_sum += arr[i]
    if curr_section <=m:
        return True

ans_min , ans_max = 1,sum(arr)

for i in range(ans_min,ans_max+1):
    if is_possible(i):
        print(i)
        break