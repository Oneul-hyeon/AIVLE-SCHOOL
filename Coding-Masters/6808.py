import sys
input = sys.stdin.readline

N, X = map(int, input().split())
# 1. 재료를 매운 기준으로 내림차순 정렬
array = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : -x[1])
# 2. 재료의 칼로리가 최대 칼로리 이내에 드는 첫 인덱스가 가장 매운 정도
for k, s in array :
    if k <= X :
        print(s)
        exit()