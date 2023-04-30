import sys
input = sys.stdin.readline

# 1. 수 입력받기
decimal = float(input())
# 2. 출력 변수 설정
ans = '0.'
# 3. while 문
while decimal!=0 :
    # 3-1. 2를 곱하고 정수부, 소수부 나누기
    integer = int(decimal*2)
    decimal = decimal*2 - integer
    # 3-2. 정수부 출력 변수에 이어붙이기
    ans += str(integer)
    if len(ans[2:]) >= 10 : break
# 4. 결과 출력
print(ans)