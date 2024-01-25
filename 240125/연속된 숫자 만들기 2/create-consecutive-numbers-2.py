a,b,c = map(int,input().split())
import sys
cnt =0
if abs(a-b) and abs(b-c) == 1:
    print(0)
if abs(a-b) ==2 or abs(b-c) ==2:
    print(1)
else:
    print(2)