n,m,p = map(int,input().split()) # 사람 수 n 메세지 정보의 수 m 확인이 필요한 메세지 번호 p

arr= [0] + [list(input().split()) for _ in range(m)]
target = arr[p]
arr_people = [False] * (n+1)
if arr[p][1] == '0':
    arr_people =[True] *(n+1)

for i in range(p,m+1):
    c,u = arr[i]
    arr_people[ord(c) - ord('A')+1] = True

for i in range(p-1,0,-1):
    if arr[i][1] == target[1]:
        arr_people[ord(arr[i][0]) - ord('A') +1] = True

for i in range(1,n+1):
    if not arr_people[i]:
        print(chr(i+64),end=' ')