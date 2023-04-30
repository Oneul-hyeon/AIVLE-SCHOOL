import sys
input = sys.stdin.readline

n, m = map(int, input().split())
empty = 0
# 1. 빈 공간의 수 구하기
if n > 1 and m > 1:
    empty = (n-2) * (m-2)
# 2. 전체 공간 - 빈 공간 출력
print(n*m - empty)