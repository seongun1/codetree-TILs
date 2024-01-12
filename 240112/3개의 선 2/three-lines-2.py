from sys import stdin
n = int(stdin.readline())

arr=[list(map(int,input().split())) for _ in range(n)]

cnt =0
#x축에 평행한 직선 3 -> 2 -> 1 -> 0 개의 순으로 진행
for i in range(11):
    for j in range(11):
        for k in range(11):
            flag = True
            for a ,b in arr:
                if a == i or a== j or a == k:
                    continue
                flag = False
            if flag: 
                cnt =1
            flag = True
            for a, b in arr:
                if a ==i or a ==j or b ==k:
                    continue
                flag =False
            if flag:
                cnt =1
            flag = True
            for a,b in arr:
                if a == i or b==j or b==k:
                    continue
                flag =False
            if flag:
                cnt =1
            flag =True
            for a,b in arr:
                if b==i or b == j or b==k:
                    continue
                flag = False
            if flag:
                cnt =1
print(cnt)