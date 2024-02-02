import sys

a = input()
b = input()

n = len(a)
m = len(b)

d = [
    [False for _ in range(m+1)]
    for _ in range(n+1)
]

a = " " + a
b = " " + b

d[0][0] = True

for j in range(m):
    for i in range(n):
        if not d[i][j]:
            continue
        
        if j != m-1 and b[j+2] == '*':
            d[i][j+2] = True

            for cur_i in range(i+1, n+1):
                if b[j+1] != '.' and a[cur_i] != b[j+1]:
                    break
                d[cur_i][j+2] = True
        
        elif b[j+1] == ".":
            d[i+1][j+1] = True
        elif b[j+1] == a[i+1]:
            d[i+1][j+1] = True

print("true" if d[n][m] else "false")


# import re

# def is_match(s, p):
#     pattern = re.compile(p)
#     return bool(pattern.fullmatch(s))

# # 입력 받기
# s = input().strip()
# p = input().strip()

# # 결과 출력
# if is_match(s, p):
#     print("true")
# else:
#     print("false")