import sys
input = sys.stdin.readline

# 1. n 입력받기
n = int(input())
num = 1
for i in range(1, n+1) :
    # 4. 한 라인에 들어갈 값 출력
    for _ in range(i) :
        print(num, end=' ')
        num+=1
    # 5. 마지막 수가 나오면 행 변환
    print('')