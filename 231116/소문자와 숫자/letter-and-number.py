x=input()

tmp =''
for i in x:
    if i.isalpha():
        tmp += i.lower()
    if i.isdigit():
        tmp += i
print(tmp)