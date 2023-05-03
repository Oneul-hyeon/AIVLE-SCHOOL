import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
# 1. 기성이의 체중 > 엘리베이터의 수용 무게 의 경우 0 출력
if m > k : print(0)
else :
    # 2. 기성이가 탔을 때의 전체 체중 - 특정 직원의 체중 > 엘리베이터의 수용 무게인 경우 그 직원은 도움이 안 되므로 빼기
    total_weight = m + sum([x[0] for x in array])
    for i in range(n-1, -1, -1) :
        if total_weight - array[i][0] > k : array.pop(i)
    # 3. 바쁜 정도가 적은 순 - 체중이 많이 나가는 순으로 정렬
    array.sort(key = lambda x : [x[1], -x[0]])
    # 4. 결과 출력
    print(len(array))
    for line in array :
        print(*line)