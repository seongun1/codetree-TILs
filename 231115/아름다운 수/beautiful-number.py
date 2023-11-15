n = int(input())
ans = []
cnt = 0

def beauty(str1):
    i = 0
    while i < n:
        idx = int(str1[i])

        if idx > len(str1[i:i+idx]):
            return False

        for j in str1[i:i+idx]:
            if j != str1[i]:
                return False
        i += idx

    return True


def print_ans():
    global cnt
    string = ""

    for i in ans:
        string += str(i)

    if beauty(string):# string -> 111, 112 ... 
        cnt += 1


def choose(cur_num):
    if cur_num == n+1:
        print_ans()
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cur_num+1)
        ans.pop()
    return 

choose(1)
print(cnt)