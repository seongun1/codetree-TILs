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

cnt = 0
for i in range(len(tmp)):
    original = tmp[i]
    tmp[i] = ')' if tmp[i] == '(' else '('  # Flip the bracket
    if is_balanced_and_valid(tmp):
        cnt += 1
    tmp[i] = original  # Restore the original bracket

print(cnt)