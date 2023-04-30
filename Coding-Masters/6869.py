import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input().rstrip().split())) for _ in range(n)]

# 1. 위치 변수 저장
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
# 2. 이중 for문
for x in range(n) :
    for y in range(n) :
        if graph[x][y] == 'X' : continue
        count = 0
        # 3. 4 방향 검사
        for dir in dirs :
            nx, ny = x+dir[0], y+dir[1]
            if nx < 0 or nx >= n or ny <0 or ny >=n : continue
            if graph[nx][ny] == 'X' : count += 1
        # 반도 체크 후 카운트
        if count == 3 : ans += 1
print(ans)