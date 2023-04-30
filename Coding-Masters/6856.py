import sys
input = sys.stdin.readline

score = [list(map(int, input().split())) for _ in range(4)]
# 1. 출력 리스트 생성
ans = [0] * 4
for i in range(4) :
    for j in range(i+1, 4) :
        # 3. 두 팀 간의 점수를 비교해 승점 추가
        if score[i][j] > score[j][i] : ans[i] += 3
        elif score[i][j] < score[j][i] : ans[j] += 3
        else :
            ans[i] += 1
            ans[j] += 1
print(*ans)