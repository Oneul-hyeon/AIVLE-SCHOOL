import sys

input = sys.stdin.readline


def check():
    # 3.
    # 3-1. 어떤 두 정점 사이 경로 확인으로 A값 결정
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a != b:
                    if graph[a][b] or (graph[a][k] and graph[k][b]):
                        graph[a][b] = True

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                if not graph[a][b]: return 'YES'
    return 'NO'


n = int(input())
B, C = 'NO', 'NO'
# 1. N+1 by N+1의 graph 생성
graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
# 2. 간선 정보 입력받기
for _ in range(n - 1):
    a, b = map(int, input().split())
    # 2-1. 간선의 양 정점이 같을 경우 B값 설정
    if a == b:
        if B == 'NO': B = 'YES'
    # 2-2. 간선의 정점 중 한 쪽이라도 존재하지 않을 경우 C값 설정
    if 1 <= a <= n and 1 <= b <= n:
        graph[a][b] = True
        graph[b][a] = True
    else:
        if C == 'NO': C = 'YES'

# 3.
A = check()
print(f'{A}\n{B}\n{C}')
