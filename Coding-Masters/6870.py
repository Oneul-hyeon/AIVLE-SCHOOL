import sys
input = sys.stdin.readline

# 1. 수 입력받기
n = int(input())
a, b = 1, 1
while n != 0 :
    # 2-1. 식(1), 식(2) 에 따라 값 설정
    a, b = b, a+b
    n-=1
# 3. 결과 출력
print(a, b)