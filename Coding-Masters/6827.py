import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. graph 생성
graph = [[0 for _ in range(n)] for _ in range(n)]
# 2. 간선 정보 입력 받기
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
# 3. a-b 양방향 간 경로가 있다면 1 입력 <- 플로이드-워셜
for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            if a != b :
                if graph[a][k] and graph[k][b] :
                    graph[a][b] = 1
# 4. 0번 인덱스의 0의 개수 출력
print(graph[0].count(0))