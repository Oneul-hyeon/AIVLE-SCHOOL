import sys, math
from collections import deque
input = sys.stdin.readline

def bfs(queue) :
    global min_d, max_d
    while queue :
        x, y = queue.popleft()
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if graph[nx][ny] == '#' : continue

            if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + 1 :
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if graph[nx][ny] == 'H' :
                    min_d = min(min_d, visited[nx][ny])
                    max_d = max(max_d, visited[nx][ny])

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
# 1. 방문 여부 겸 거리 저장 리스트 설정
visited = [[0 for _ in range(n)] for _ in range(n)]
# 2. 방향 리스트 설정
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 3. 허브의 위치를 큐에 삽입
queue = deque([])
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 'G' :
            queue.append((i, j))
# 4. BFS 실행
min_d, max_d = math.inf, -math.inf
bfs(queue)
# 5. 결과 출력
print(max_d - min_d)