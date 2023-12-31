#n:총 개발자의 수 k:전염병 옮길 수 있는 횟수 p:초기에 병이 걸린 개발자 T:악수를 한 횟수
n,k,p,T = map(int,input().split())
arr= [0 for _ in range(n+1)] #개발자들의 전염현황
arr_chance = [k for _ in range(n+1)] # 개발자들이 감염시킬 수 있는 횟수
virus = []
for _ in range(T):
    virus.append(list(map(int,input().split())))
virus.sort(key = lambda x : x[0])
arr[p] = 1
for v in virus: #서로 악수를 하는 경우
    if arr[v[1]] == 1 and arr[v[2]] ==1: #둘 다 감염됐을 경우
        arr_chance[v[1]] -= 1
        arr_chance[v[2]] -= 1
    if arr[v[1]] == 1 and arr_chance[v[1]] > 0: #감염됐고, 감염시킬수 있는 횟수가 0 이상인 경우
        arr[v[2]] =1
        arr_chance[v[1]] -=1
    elif arr[v[2]] ==1 and arr_chance[v[2]] >0:
        arr[v[1]] =1
        arr_chance[v[2]] -=1
for i in range(1,len(arr)):
    print(arr[i],end='')