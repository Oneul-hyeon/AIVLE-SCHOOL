import sys
input = sys.stdin.readline


n = int(input())
# 1. 현재 위치 설정
a, b = 0, 0
# 2. 입력에 따른 위치 재설정
for _ in range(n) :
    d, x = map(int, input().split())
    if d == 1 : a+=x
    elif d == 2 : b+=x
    elif d == 3 : a-=x
    else : b-=x
# 3. 최종 위치 출력
print(a, b)