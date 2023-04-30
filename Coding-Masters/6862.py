import sys
input = sys.stdin.readline

n = int(input())
# 1. 배열 정렬하기
array = sorted(list(map(int, input().split())))
# 2. (1번 - 2번)과 (n-1번 - n-2번) 차이 비교
# 3. 해당 원소를 뺀 배열의 평준화 정도 출력
if array[1] - array[0] > array[n-1] - array[n-2] :
    print(array[n-1] - array[1])
else :
    print(array[n-2] - array[0])
