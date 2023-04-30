import sys
input = sys.stdin.readline

a, b = map(int, input().split())
# 1. 리스트 생성
array = [0] * 101
# 2. 초기 값 설정
array[1], array[2] = 1, 1
# 3. 피보나치를 위한 변수 생성
n1, n2 = array[1], array[2]
# 4. 리스트 인덱스 변수 생성
i = 3
while i <= 101 :
    # 5-1. 다음 피보나치 수 생성
    n = n1 + n2
    # 5-2. 생성된 피보나치 수만큼 피보나치 수 입력
    for x in range(i, i+n) :
        if x == 101 : break
        else : array[x] = n
    # 5-3. i값 재설정
    i += n
    # 5-4 n1, n2 값 재설정
    n1, n2 = n, n1
# 4. a항부터 b항까지의 합 출력
print(sum(array[a:b+1]))