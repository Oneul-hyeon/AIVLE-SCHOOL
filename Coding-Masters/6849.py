import sys
input = sys.stdin.readline

n = int(input())
# 1. 카드 입력받기
card = list(map(int, input().split()))
# 2. left, right 설정
left, right = 0, n-1
find_card = 1
while left<=right :
    # 4. 찾는 카드 번호가 left, right 인덱스에 있는지 확인
    # 5. left 인덱스에 있을 경우
    if card[left] == find_card : left+= 1
    # 6. right 인덱스에 있을 경우
    elif card[right] == find_card : right -= 1
    # 7. 없을 경우 while문 탈출
    else : break
    # 8. while문으로 찾는 카드 번호가 n까지 왔다면 YES 출력 후 프로그램 종료
    if find_card == n :
        print('YES')
        sys.exit()
    find_card += 1
print('NO')