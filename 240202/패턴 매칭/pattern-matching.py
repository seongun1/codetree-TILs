# import sys

# s = input()
# p = input()

# n = len(s)
# m = len(p)


# def possible():
#     for i in range(1,n+1):
#         if (s[i-1] == p[i-1]) or (p[i-1] == '.'):
#             continue
#         elif (p[i-1] == '*'):
#             for j in range(i,n+1):
#                 if s[i-1] == s[j-1]:
#                     return True
                
#         else:
#             return False
#     return True

# if possible():
#     print("true")
# else:
#     print("false")
import re

def is_match(s, p):
    pattern = re.compile(p)
    return bool(pattern.fullmatch(s))

# 입력 받기
s = input().strip()
p = input().strip()

# 결과 출력
if is_match(s, p):
    print("true")
else:
    print("false")