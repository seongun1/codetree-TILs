string=input()
flag = False
fflag = False
for i in range(len(string)-1):
    if string[i] =='e' and string[i+1] == 'e':
        flag =True

for i in range(len(string)-1):
    if string[i] =='a' and string[i+1] == 'b':
        fflag =True
if flag:
    print('Yes',end=' ')
else:
    print("No",end=' ')
if fflag:
    print('Yes',end=' ')
else:
    print("No",end=' ')