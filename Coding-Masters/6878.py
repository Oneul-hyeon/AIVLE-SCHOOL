import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. 사무실 입력받기
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# 2. 사무실 정보로 직원의 위치를 리스트에 저장
staff_index = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            staff_index.append((i, j))

# 3. 최솟값 변수 선언
min_ans = int(1e9)
# 4. 이중 for 문을 통해 특정 위치에 전열기 3개가 있을 때 각 직원과의 거리 합 구하기
for i in range(n) :
    for j in range(m) :
        ans = 0
        for staff in staff_index :
            ans += (abs(staff[0]-i) + abs(staff[1]-j)) * 3
        # 5. 최솟값 비교 후 업데이트
        if min_ans>ans : min_ans = ans
print(min_ans)