import sys
input = sys.stdin.readline

# 1. 세 변의 길이 입력받기
a, b, c = sorted(map(int, input().split()))
# 2. 식이 성립되는지 확인
# 3. 결과 출력
print('YES') if c**2 == a**2 + b**2 else print('NO')