#n명이 m가지의 치즈를 먹었음. 정확히 하나가 상했다.
#특정 사람이 어떤 치즈를 언제 먹었는지의 기록 d번
#특정 사람이 언제 아팠는지에 대한 기록이 s번(기록된 것 외에 다른사람이 아플 수 있다.)
#약이 최대 몇 개나 필요한가?

def find_cnt(arr):
    cnt =0
    for a in arr:
        if a== True:
            cnt +=1
    return cnt

n,m,d,s = map(int,input().split()) #n명이/ m가지의 치즈를 / d개의 먹은 기록 / 아팠는지 기록이 s
arr_d = [list(map(int,input().split())) for _ in range(d)] #몇 번째 사람이 /  몇 번째 치즈를 / 언제 먹었는지
arr_s = [list(map(int,input().split())) for _ in range (s)] #몇 번째 사람이 / 언제 아팠는지
arr=[False] *(n+1) #아프면 True
max_cnt =0
tmp=[]
for i in range(s):
    p_i,t_i = arr_s[i]
    for j in range(d):
        p_j,m_j,t_j = arr_d[j]
        if p_i == p_j and t_j < t_i: # 아프기 전의 먹은 치즈들(의심가는 치즈)을 다 tmp 배열에 넣는다.
            tmp.append([p_j,m_j,t_j])
if s>1:
    ans =[] # 겹치는 치즈를 구하는 배열
    for s in range(len(tmp)):
        a1,b1,c1 = tmp[s]
        for ss in range(len(tmp)):
            if s==ss:
                continue
            a2,b2,c2 = tmp[ss]
            if b1 == b2:
                ans.append([a1,b1,c1])
                break
else:
    ans =tmp.copy()


for t in range(len(ans)): #의심가는 치즈 중 하나만 상했을때를 가정 , 최대 약의 갯수를 구한다.
    a,b,c = ans[t] #만약 이것이 상했다면?
    for k in range(d):
        p,m,t = arr_d[k]
        if b == m:
            arr[p] = True
    max_cnt = max(max_cnt,find_cnt(arr))
    arr = [False] *(n+1)

print(max_cnt)