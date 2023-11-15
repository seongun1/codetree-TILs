k,n = map(int,input().split())

ans = []

def print_ans():
    for e in ans:
        print(e,end=" ")
    print()

def choose(cur_num): # cur_num은 해당 자리 위치
    if cur_num == n+1:
        print_ans()
        return
    
    for i in range(1, k + 1):  # Iterate from 1 to k
        ans.append(i)
        choose(cur_num + 1)
        ans.pop()

    return

choose(1)