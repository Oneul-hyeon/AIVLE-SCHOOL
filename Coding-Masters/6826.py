import sys
input = sys.stdin.readline

# 2. 재귀 함수 설정
def dac(a, b, c):
    # 2-1. 종료 조건 설정
    if b == 1:
        return a % c
    # 2-2. b가 짝수일 경우
    elif b % 2 == 0:
        return (dac(a,b//2,c)**2)%c
    # 2-3. b가 홀수일 경우
    else:
        return ((dac(a,b//2,c)**2)*a)%c
# 1. k, n 입력받기
k, n = map(int, input().split())
# 3. 재귀함수 실행
print(dac(k, n, 1000000007))