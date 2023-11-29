# n,m,c = map(int,input().split())

# arr = [
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# def thief1(cur_x):
#     global max_value, select_x, select_y
#     if cur_x == n: # 벗어남
#         return

#     cur_y = 0

#     while cur_y <= n-m:
#         w = 0
#         weights = []
#         for k in range(m):
#             w += arr[cur_x][cur_y + k]
#             weights.append(arr[cur_x][cur_y + k])
        
#         value = 0
#         if w <= c:
#             for i in range(m):
#                 value += weights[i] ** 2
#         else: # C 보다 크니까 적절하게 weight를 골라야한다
#             weights.sort()
#             while w > c:
#                 w -= weights[0]
#                 weights.pop(0)
            
#             for i in range(len(weights)):
#                 value += weights[i] ** 2
        
#         if value >= max_value:
#             max_value = value 
#             select_x, select_y = cur_x, cur_y
        
#         cur_y += 1
    
#     thief1(cur_x+1)

# # thief1 을 거치면서 select_x, select_y는 현재 도둑1이 있는 부분이다.
# def thief2(cur_x):
#     global max_value2
#     if cur_x == n: # 벗어남
#         return

#     cur_y = 0

#     if select_x <= cur_x <= select_y: # 겹침
#         return
    
#     while cur_y <= n-m:
#         w = 0
#         weights = []
#         for k in range(m):
#             w += arr[cur_x][cur_y + k]
#             weights.append(arr[cur_x][cur_y + k])
        
#         value = 0
#         if w <= c:
#             for i in range(m):
#                 value += weights[i] ** 2
#         else: # C 보다 크니까 적절하게 weight를 골라야한다
#             weights.sort()
#             while w > c:
#                 w -= weights[0]
#                 weights.pop(0)
            
#             for i in range(len(weights)):
#                 value += weights[i] ** 2
        
#         if value >= max_value2:
#             max_value2 = value 
#             select_xx, select_yy = cur_x, cur_y
        
#         cur_y += 1
    
#     thief2(cur_x+1)
# max_value, max_value2, select_x, select_y, select_xx, select_yy = 0,0,0,0,0,0
# thief1(0)
# thief2(0)

# print(max_value + max_value2)

N, M, C = map(int, input().split())
rooms = [
    list(map(int, input().split()))
    for _ in range(N)
]

def thief1(cur_i):
    global max_value, selected_i, selected_j
    if cur_i == N:
        return
    cur_j = 0
    while cur_j <= N - M:
        weight = 0
        weights = []
        for k in range(M):
            weight += rooms[cur_i][cur_j + k]
            weights.append(rooms[cur_i][cur_j + k])
        value = 0
        if weight <= C:
            for i in range(M):
                value += weights[i] ** 2
        else: # C 보다 크니까 적절하게 weight를 골라야한다
            weights.sort()
            while weight > C:
                weight -= weights[0]
                weights.pop(0)
            
            for i in range(len(weights)):
                value += weights[i] ** 2
        if value > max_value:
            max_value = value
            selected_i, selected_j = cur_i, cur_j
        cur_j += 1
    thief1(cur_i + 1)

def thief2(cur_i):
    global max_value2
    if cur_i == N:
        return
    cur_j = 0
    if cur_i == selected_i:
        while cur_j <= selected_j - M:
            weight = 0
            weights = []
            for k in range(M):
                weight += rooms[cur_i][cur_j + k]
                weights.append(rooms[cur_i][cur_j + k])
            value = 0
            if weight <= C:
                for i in range(M):
                    value += weights[i] ** 2
            else: # C 보다 크니까 적절하게 weight를 골라야한다
                weights.sort()
                while weight > C:
                    weight -= weights[0]
                    weights.pop(0)
                
                for i in range(len(weights)):
                    value += weights[i] ** 2
            if value > max_value2:
                max_value2 = value
            cur_j += 1

        cur_j = selected_j + M
        while cur_j <= N - M:
            weight = 0
            weights = []
            for k in range(M):
                weight += rooms[cur_i][cur_j + k]
                weights.append(rooms[cur_i][cur_j + k])
            value = 0
            if weight <= C:
                for i in range(M):
                    value += weights[i] ** 2
            else: # C 보다 크니까 적절하게 weight를 골라야한다
                weights.sort()
                while weight > C:
                    weight -= weights[0]
                    weights.pop(0)
                
                for i in range(len(weights)):
                    value += weights[i] ** 2
            if value > max_value2:
                max_value2 = value
            cur_j += 1

    else:
        while cur_j <= N - M:
            weight = 0
            weights = []
            for k in range(M):
                weight += rooms[cur_i][cur_j + k]
                weights.append(rooms[cur_i][cur_j + k])
            value = 0
            if weight <= C:
                for i in range(M):
                    value += weights[i] ** 2
            else: # C 보다 크니까 적절하게 weight를 골라야한다
                weights.sort()
                while weight > C:
                    weight -= weights[0]
                    weights.pop(0)
                
                for i in range(len(weights)):
                    value += weights[i] ** 2
            if value > max_value2:
                max_value2 = value
            cur_j += 1
    thief2(cur_i + 1)

max_value = 0
selected_i, selected_j = 0, 0
thief1(0)

max_value2 = 0
thief2(0)

print(max_value + max_value2)