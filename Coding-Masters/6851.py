import sys
input = sys.stdin.readline

# 5. 재귀 함수 선언
def check(num) :
    # 5-1. 종료 조건 설정 - 남은 문자열이 없으면 return
    if num == '' :
        return
    # 5-2. 특정 수가 n과 나눠 떨어지면 예쁜 수 - YES 출력 후 프로그램 종료
    if int(n)%int(num) == 0 :
        print('YES')
        sys.exit()
    else :
        # 5-3. 나눠 떨어지지 않을 경우
        check(num[1:])
        check(num[:-1])

# 1. n 입력받기
n = input().rstrip()
# 2. n의 맨 앞에 수 1개를 떼어내어 재귀함수의 인자로 넣고 실행
check(n[1:])
# 3. n의 맨 뒤에 수 1개를 떼어내어 재귀함수의 인자로 넣고 실행
check(n[:-1])
# 4. 예쁜 수가 아닐 경우 NO 출력
print('NO')