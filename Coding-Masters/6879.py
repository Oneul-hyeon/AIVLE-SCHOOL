import sys
input = sys.stdin.readline

# 1. 각 월의 말일이 담긴 리스트 생성
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 2. 오늘 날짜 입력받기
month, day = map(int, input().split())
# 3. 10월 미만일 경우
if month < 10 :
    # 3-1. for문
    for potential_day in range(month, days[month], 10) :
        # 3-2. 팰린드롬이 가능한 날짜 확인
        if potential_day > day :
            print(month, potential_day)
            break
    # 3-3. 가능한 날짜가 없다면 다음월의 첫 날 출력
    else :
        if month == 9 : print(month+1, 1)
        else : print(month+1, month+1)
# 10월 이후일 경우
else :
    # 4-1. 해당 월을 뒤집은 문자열이 오늘 날짜보다 크면 출력
    if int(str(month)[::-1]) > day :
        print(month, str(month[::-1]))
    # 4-2. 오늘 날짜가 더 큰 경우 다음 월 출력
    else :
        # 4-3. 12월의 경우 1월 1일 출력
        if month == 12 : print(1, 1)
        else : print(month+1, str(month+1)[::-1])