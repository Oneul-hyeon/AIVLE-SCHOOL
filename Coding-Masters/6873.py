import sys
input = sys.stdin.readline

n = int(input())
# 1. 출력 문자열, i 설정
ans, i = '', 1
while n != 0 :
    # 2. n을 i로 나눈 몫과 나머지 구하기
    n, mod = divmod(n, i)
    # 2-2. 나머지 문자열에 붙이기
    ans = str(mod) + ans
    # 2-3. i 증가
    i += 1
# 3. 결과 출력
print(ans)
