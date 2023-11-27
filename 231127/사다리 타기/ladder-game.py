n,m = map(int,input().split())

# [ 라인번호, 숫자 ]
arr = [[i,i] for i in range(1,n+1)] # [[1, 1], [2, 2], [3, 3], [4, 4]]

line = []
for i in range(m):
    a,b = map(int,input().split())
    line.append((a,b))

line.sort(key = lambda x : x[1])
#print(line)

result = []

def move(line):
    res = []
    for i in range(1,n+1):
        cur_idx = i
        height = 0 # 얘도 증가해야함

        for j in line:
            a,b = j

            if a == cur_idx and height <= b:
                cur_idx = a+1
            
            elif a == cur_idx - 1 and height <= b:
                cur_idx = a 

            height = b
        res.insert(cur_idx-1,i)
    return res
result = move(line)
#print(result) # 잘 들어옴

temp_line = []
ans = []
min_cnt = 200

def print_ans():
    global min_cnt
    ans = move(temp_line)

    for i in range(n):
        if ans[i] != result[i]:
            return

    #print(ans)
    dup_cnt = 0
    for i in range(len(temp_line)-1):
        for j in range(i+1, len(temp_line)):
            if (temp_line[i] == temp_line[j]):
                dup_cnt += 1
    if min_cnt >= len(temp_line):
        min_cnt = len(temp_line) - dup_cnt



def putLine(cur_num):
    if cur_num == n+1:
        print_ans()
        return 

    for i in range(cur_num, len(line)):
        temp_line.append(line[i])
        putLine(cur_num + 1)
        temp_line.pop()
putLine(1)

if min_cnt == 200:
    print(0)
else:
    print(min_cnt)