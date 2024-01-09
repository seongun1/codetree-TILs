#n명이 m가지의 치즈를 먹었음. 정확히 하나가 상했다.
#특정 사람이 어떤 치즈를 언제 먹었는지의 기록 d번
#특정 사람이 언제 아팠는지에 대한 기록이 s번(기록된 것 외에 다른사람이 아플 수 있다.)
#약이 최대 몇 개나 필요한가?

n,m,d,s = map(int,input().split())
arr_d = [list(map(int,input().split())) for _ in range(d)] #몇 번째 사람이 /  몇 번쨰 치즈를 / 언제 먹었는지
arr_s = [list(map(int,input().split())) for _ in range (s)] #몇 번째 사람이 / 언제 아팠는지
arr=[False] *(n+1) #아프면 True

tmp=[]
for i in range(s):
    p_i,t_i = arr_s[i]
    for j in range(d):
        p_j,m_j,t_j = arr_d[j]
        if p_i == p_j and t_j < t_i:
            tmp.append([p_j,m_j,t_j])
    for t in range(len(tmp)):
        a,b,c = tmp[t]
        for k in range(d):
            p,m,t = arr_d[k]
            if b == m:
                arr[p] = True
cnt =0
for a in arr:
    if a== True:
        cnt +=1
print(cnt)