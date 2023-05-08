import sys
input = sys.stdin.readline
def dfs(count, block, idx) :
    global ans
    # 3-1. 종료 조건 설정
    if count == k :
        ans += 1
        return
    for i in range(idx, block) :
        if block - i <= i :
            return
        dfs(count+1, block - i, i+1)

# 1. n, k 입력받기
n = int(input())
k = int(input())
ans = 0
if k == 1 : print(1)
else :
    if k == 2 : max_h = n - 1
    elif k == 3 : max_h = n - 3
    elif k == 4 : max_h = n - 6
    # 3. 재귀 함수 실행
    dfs(1,n,1)
    print(ans)