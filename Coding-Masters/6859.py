import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 1. k를 n으로 나눈 몫 구하기
# 2. 몫과 n을 곱해 출력하기
print(n * (k//n))