n,m = map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(n)]
#행복한 수열 = 연속하여 m 개 이상의 동일한 원소가 나오는 순간이 존재
ans =0

#행을 검사
def search_row(arr,n,m):
    global ans
    for i in range(n):
        cnt =0
        for j in range(n-m+1):
            for k in range(m):
                if arr[i][j] != arr[i][j+k]:
                    break
            else:
                cnt = 1
                break
        if cnt ==1:
            ans +=1

def search_coloum(arr,n,m):
    global ans
    for i in range(n):
        cnt =0
        for j in range(n-m+1):
            for k in range(m):
                if arr[j][i] != arr[j+k][i]:
                    break
            else:
                cnt =1
                break
        if cnt == 1:
            ans +=1
search_coloum(arr,n,m)
search_row(arr,n,m)
print(ans)