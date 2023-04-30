import sys
input = sys.stdin.readline

h, w = map(int, input().split())
# 1. 두 점의 위치 입력받기
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
# 2. 두 점의 x 위치, y 위치가 각각 다르면  yes 출력
if p1[0] != p2[0] and p1[1] != p2[1] : print('YES')
else : print('NO')