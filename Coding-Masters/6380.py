import sys
from collections import Counter
input = sys.stdin.readline

# 1. 재귀함수 설정
def check() :
    global ball
    # k개의 구슬이 연속으로 이어진다면 제거
    # k개의 구슬이 연속으로 이어지지 않는다면 True 반환
    for i in range(len(ball)) :
        if len(ball[i:i+k]) == k and len(set(ball[i:i+k])) == 1 :
            ball = ball[:i] + ball[i+k:]
            return False
    return True

n = int(input())
k = int(input())
ball = input().rstrip()
# 2. 재귀함수에서 True가 반환된 때까지 실행
while True :
    if check() : break
# 3. Counter를 사용해 각 공의 개수 확인
counter = Counter(ball)
# 4. 결과 출력
print(counter['R'] + counter['G'] * 2 + counter['B'] * 3)