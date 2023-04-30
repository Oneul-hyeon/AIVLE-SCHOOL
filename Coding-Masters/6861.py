import sys
input = sys.stdin.readline

password = input().rstrip()

# 1. 현재 인덱스 값, i값 설정
now_index = 0
i = 0
ans = ''
while now_index < len(password) :
    # 3. 암호화한 문자열의 특정 인덱스만 뽑기
    ans += password[now_index]
    i += 1
    now_index += i