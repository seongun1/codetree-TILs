n,m = map(int,input().split())

line = list()
select_line = list()
ans = m

for i in range(m):
    a,b = tuple(map(int,input().split()))
    line.append((b,a-1))

line.sort()

def possible():
    # num1 은 초기값에 대한 결과
    num1,num2 = [i for i in range(n)], [i for i in range(n)]

    # 한번에 결과 찾기
    for _, idx in line:
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]
    for _, idx in select_line:
        num2[idx], num2[idx+1] = num2[idx+1], num2[idx]
    
    for i in range(n):
        if num1[i] != num2[i]:
            return False
    return True

def find_min(cnt):
    global ans

    if cnt == m:
        if possible():
            ans = min(ans, len(select_line))
        return
    
    select_line.append(line[cnt])
    find_min(cnt+1)
    select_line.pop()
    find_min(cnt+1)


find_min(0)
print(ans)