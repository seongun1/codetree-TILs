a=input()
b=input()
a_d=''
b_d=''
for i in a:
    if i.isdigit():
        a_d +=i
for i in b:
    if i.isdigit():
        b_d +=i
print(int(a_d) + int(b_d))