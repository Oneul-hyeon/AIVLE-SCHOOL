import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1. 출력 변수 설정
ans = 0
max_h = -int(1e9)
for tree in array :
    if max_h < tree :
        # 3. 루프를 돌면서 최댓값 설정
        max_h = tree
        # 4. 볼 수 있는 나무 카운트
        ans += 1
# 5. 결과 출력
print(ans)