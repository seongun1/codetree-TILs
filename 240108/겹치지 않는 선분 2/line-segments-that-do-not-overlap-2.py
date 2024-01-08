n = int(input())

lines = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append(((x1, 0) , (x2, 1)))

cross = 0
for i in range(n):
    for j in range(n):
        # 자기 자신은 제외
        if j == i:
            continue

        # 첫번째 선분과 두번째 선분
        line1 = lines[i]
        line2 = lines[j]

        # 첫번째 선분의 시작점 x좌표가 두번째 선분의 시작점 x좌표보다 작고
        # 첫번째 선분의 끝점 x좌표가 두번째 선분의 끝점 x좌표보다 크면
        # 교차하므로 교차하는 선분 2개 증가
        if (line1[0][0] < line2[0][0]) and (line1[1][0] > line2[1][0]):
            cross += 2

# 선분의 개수 중 교차하는 선분 뺀 값
ans = n - cross

# 서로 교차하는 선분이 2개 이상이면 뺀 값이 음수가 나올 수 있으므로 
# ans가 음수면 교차하지 않는 선분이 없다는 의미로 0 출력
if ans < 0:
    print(0)
else:
    print(ans)