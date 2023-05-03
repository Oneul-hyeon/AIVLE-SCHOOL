import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 1. 이중 for문으로 직사각형 모양 설정
for x in range(1, n+1) :
    for y in range(1, m+1) :
        for i in range(n-x+1) :
            # 만들어진 직사각형 안의 수 합 구하기
            for j in range(m-y+1) :
                summation = 0
                for k in range(i, i + x):
                    summation += sum(graph[k][j:j+y])
                # 4. 해당 수들의 합이 10인지 확인
                if summation == 10 : ans += 1
# 5. 결과 출력
print(ans)