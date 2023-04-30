import sys
input = sys.stdin.readline


n = int(input())
string = input().rstrip()
# 1. 출력 문자열 변수 선언
ans =''
# 2. 반대쌍 정보에 따라 출력 문자열 만들기
for i in range(n) :
    if string[i] == 'A' : ans += 'T'
    elif string[i] == 'T' : ans += 'A'
    elif string[i] == 'G' : ans += 'C'
    else : ans += 'G'
# 3. 결과출력
print(ans)