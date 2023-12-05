string = input()

operand, alpha = list(), list()

for i in string:
    if i in ['+', '-', '*']:
        operand.append(i)
    else:
        alpha.append(i)

unique_alpha = {
    a:0
    for a in set(alpha)
}

ans = []
max_val = 0

def println():
    global max_val, unique_alpha

    for i,k in enumerate(unique_alpha.keys()):
        unique_alpha[k] = ans[i]
    
    cnt = unique_alpha[alpha[0]]

    for i, oper in enumerate(operand):
        next_val = unique_alpha[alpha[i+1]]
        if oper == '+':
            cnt += next_val
        elif oper == '-':
            cnt -= next_val
        else:
            cnt *= next_val
    
    max_val = max(max_val, cnt)


def choose(cur):
    if cur == len(alpha):
        println()
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cur+1)
        ans.pop()
    
    return

choose(0)
print(max_val)