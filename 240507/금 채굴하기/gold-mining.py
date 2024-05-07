n,m = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(n)]

def count_gold():
    max_ans = 0
    for k in range(50):
        if k>n:
            break
        for i in range(n):
            for j in range(n):
                gold = 0
                #마름모 만들기
                for rr in range(n):
                    for cc in range(n):
                        if arr[rr][cc] == 1 and abs(i-rr) + abs(j - cc) <= k:
                            gold += 1
                spend = k *k + (k+1) * (k+1)
                profit = (gold*m) - spend
                if profit >= 0:
                    max_ans = max(gold,max_ans)
    return max_ans
print(count_gold())