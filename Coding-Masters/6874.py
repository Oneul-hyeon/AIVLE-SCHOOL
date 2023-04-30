import sys
input = sys.stdin.readline

# 1. 문자열 입력받기
string = input().rstrip()
# 2. 숫자 저장을 위한 변수, 결과값 변수 생성
num, ans = '', 0

for i in range(len(string)) :
    # 3-1. 숫자 저장 변수에 수가 들어잇으면서 알파벳이 나온 경우
    if num and string[i].isalpha() :
        ans += int(num)
        num = ''
    # 3-2. 숫자가 나온 경우
    elif not string[i].isalpha() :
        num += string[i]
# 4. for문 탈출 후 숫자 저장 변수에 수가 있는지 확인
if num : ans += int(num)
# 5. 결과값 출력
print(ans)