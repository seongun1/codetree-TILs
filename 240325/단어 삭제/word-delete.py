def is_correct(index):
    for w in range(len(word)):
        if string[index+w] != word[w]:
            return False
    return True


tmp_s = list(input())
word = list(input())
string =[' ']*401

for i in range(len(tmp_s)):
    string[i] = tmp_s[i]
#print(string)


index = 0
while (index < len(string)):
    flag = False
    if string[index] == word[0]:
        flag = is_correct(index)
    if flag: #맞을 경우
        left,right = index,index+len(word)
        index = 0 #인덱스 초기화
        if left ==0:
            string = string[right:]
        else:
            string = string[:left] +string[right:]
        #print(left,right)
        #print(''.join(string))
    index +=1
    if flag:
        index -=1

print(''.join(string))