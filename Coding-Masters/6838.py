import sys
from collections import deque
input = sys.stdin.readline

def check() :
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == 'N' : return i, j

def bfs(i, j) :
    queue = deque([])
    queue.append((i, j))
    visited[i][j] = True
    while queue :
        x, y = queue.popleft()
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if graph[nx][ny] == 'W' : visited[nx][ny] = True
            if not visited[nx][ny] :
                visited[nx][ny] = True
                queue.append((nx, ny))
    return

n = 8
graph = [list(input().rstrip()) for _ in range(n)]
# 1. 방문 여부 리스트 생성
visited = [[False for _ in range(n)] for _ in range(n)]
# 2. 방향 변수 리스트 생성
dirs = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1), (-1, -2), (1, -2)]
# 3. 현재 나이트의 위치 찾기
i, j = check()
# 4. BFS 실행
bfs(i, j)
# 5. 방문하지 않은 인덱스 찾기
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            print('NO')
            exit()
else :
    print('YES')
