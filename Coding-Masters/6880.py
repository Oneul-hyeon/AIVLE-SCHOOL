import sys
input = sys.stdin.readline
# 1. 수 입력받기
X, A, B, C, N = map(int, input().split())
# 2. for문
# 3. X값 재설정
for _ in range(N) : X = (X*A+B)%C
# 4. 결과 출력
print(X)