import sys

string = input()

alpha, oper, ans = list(),list(),list()

max_val = -sys.maxsize

for i in string:
    if i.isalpha():
        alpha.append(i)
    else:
        oper.append(i)

dic = {}
for i in alpha:
    dic[i] = 0

def calc():

    for i, k in enumerate(dic.keys()):
        dic[k] = ans[i]
    
    val = dic[alpha[0]]
    for i, op in enumerate(oper):
        next_val = dic[alpha[i+1]]
        if op == '+':
            val += next_val
        elif op == '-':
            val -= next_val
        elif op == '*':
            val *= next_val
    return val

def choose(idx):
    global max_val

    if idx == len(dic):
        max_val = max(max_val, calc())
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(idx+1)
        ans.pop()

choose(0)
print(max_val)