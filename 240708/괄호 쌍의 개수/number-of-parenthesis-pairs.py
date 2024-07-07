tmp = input()
tmp = list(tmp)

def is_balanced_and_valid(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def is_same(s):
    balance =0
    for char in s:
        if char == '(':
            balance +=1
        else:
            balance -=1
    if balance !=0:
        return False
    return True

cnt = 0
for i in range(len(tmp)):
    original = tmp[i]
    tmp[i] = ')' if tmp[i] == '(' else '('  
    if not is_same(tmp):
        tmp[i] = original
        continue
    if is_balanced_and_valid(tmp):
        cnt += 1
    tmp[i] = original

print(cnt)