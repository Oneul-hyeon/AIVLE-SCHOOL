import sys

input = sys.stdin.readline

n = int(input())
# 1. 주어진 수가 짝수라면 2 출력
if n%2 == 0 : print(2)
else :
    # 2. 홀수일 경우 배열을 생성해 n까지 소수 여부 저장
    array = [True] * (n+1)
    array[0], array[1] = False, False
    for i in range(2, n+1) :
        if not array[i] :
            for j in range(2*i, n+1, i) :
                array[j] = False
    # 3. 약수를 찾으면서 해당 약수가 소수일 경우 값 출력
    for i in range(3, n+1) :
        if n%i == 0 :
            if array[i] :
                print(i)
                break