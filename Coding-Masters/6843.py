import sys
from collections import deque
input = sys.stdin.readline

# 1번 조건 - 1
def check_point() :
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if graph[i][j] == '.' :
                return i, j

def bfs_1(i, j) :
    queue = deque([])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True
    queue.append((i, j))
    while queue :
        x, y = queue.popleft()
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if graph[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if graph[i][j] == '.' and not visited[i][j] : return False
    return True
def check_edge(visited) :
    queue = deque([])
    visited[0][0] = 1
    queue.append((0, 0))
    while queue :
        x, y = queue.popleft()
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if graph[nx][ny] == '#' and not visited[nx][ny] :
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return visited
def bfs_2(i, j) :
    queue = deque([])
    queue.append((i, j))
    num = 1
    while queue :
        x, y = queue.popleft()
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if graph[nx][ny] == '#' and not visited[nx][ny] :
                num += 1
                visited[nx][ny] = num
                queue.append((nx, ny))
    return
n = int(input())
N, M = 10, 20
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n) :
    graph = [list(input().rstrip()) for _ in range(N)]
    # 1-1. 이중 for문을 돌면서 .이 있는 한 개의 인덱스를 구한다.
    i, j = check_point()
    # 1-2. bfs 실행
    # 1-3. 방문하지 않은 .이 있다면 False, 모두 방문했다면 True 반환
    ans_1 = bfs_1(i, j)

    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 2-1. 테두리와 연결된 '#'은 모두 방문 처리
    visited = check_edge(visited)
    # 2-2. 이중 for문을 돌면서 방문하지 않은 '#'에 대해 BFS 실행
    for i in range(1, N - 1) :
        for j in range(1, M - 1) :
            if graph[i][j] == '#' and visited[i][j] == 0:
                visited[i][j] = 1
                bfs_2(i, j)
    # 2-3. 2번 보건을 만족하는 덩어리가 있다면 True, 없다면 False 반환
    ans_2 = False
    for i in range(1, N - 1) :
        for j in range(1, M - 1) :
            if visited[i][j] >= 6 : ans_2 = True
    # 결과 출력
    if ans_1 and ans_2 : print(3)
    elif ans_1 : print(1)
    elif ans_2 : print(2)
    else : print(0)