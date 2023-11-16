a=input()
tmp=''
for i in a:
    if ord('A') <= ord(i) <= ord('Z'):
        tmp+=i.lower()
    elif ord('a') <= ord(i) <= ord('z'):
        tmp+=i.upper()
print(tmp)