import sys
input = sys.stdin.readline

t = int(input())
array = sorted(list(map(int, input().split())))

# 1. 작심삼일을 하는 최대 날짜 변수 설정
max_day = 0
for day in array :
    # 3. 해당일이 1에서 선언한 최대 날짜 값 이내에 들 경우 변수 값 업데이트
    if day <= max_day : max_day = day + 3
    # 4. 해당일이 1에서 선언한 최대 날짜 값 이내에 들지 않을 경우 for문 탈출
    else : break
# 5. 결과 출력
print(max_day)