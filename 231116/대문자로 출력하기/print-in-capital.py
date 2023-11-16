x=input()
tmp=''
for i in x:
    if i.isalpha():
        tmp += i.upper()
print(tmp)