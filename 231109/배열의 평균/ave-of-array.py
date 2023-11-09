arr=[list(map(int,input().split())) for _ in range(2)]
for i in range(2):
    print(f"{sum(arr[i])/len(arr[i]):.1f}",end=' ')
print()
for i in range(4):
    print(f"{(arr[0][i] + arr[1][i])/2:.1f}",end=' ')
tmp =0
print()
for i in range(2):
    tmp += sum(arr[i])
print(f"{tmp/8:.1f}")