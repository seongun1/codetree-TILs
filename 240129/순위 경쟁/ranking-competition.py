n=int(input())
cnt_a,cnt_b,cnt_c = 0,0,0
arr=[]
arr.append('abc')

for _ in range(n):
    person,score = input().split()
    if person =='A':
        cnt_a += int(score)
    elif person =='B':
        cnt_b += int(score)
    elif person =='C':
        cnt_c += int(score)
    if cnt_a > cnt_b and cnt_a > cnt_c: #a
        arr.append('a')
    elif cnt_b > cnt_c and cnt_b > cnt_a:#b
        arr.append('b')
    elif cnt_c > cnt_a and cnt_c > cnt_b: #c
        arr.append('c')
    elif cnt_a == cnt_b and cnt_a >cnt_c:#ab
        arr.append('ab')
    elif cnt_a == cnt_c and cnt_a > cnt_b: #ac
        arr.append('ac')
    elif cnt_b == cnt_c and cnt_b > cnt_a: #bc
        arr.append('bc')
    elif cnt_a == cnt_b == cnt_c:#abc
        arr.append('abc')
cnt =0
for i in range(n):
    if arr[i] != arr[i+1]:
        cnt +=1
print(cnt)