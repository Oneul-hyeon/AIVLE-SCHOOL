import sys
input = sys.stdin.readline

# 1. 참가자들의 실력을 내림차순으로 정렬
array = sorted(list(map(int, input().split())), reverse = True)
ans = 0

for x in array :
    if ans <0 : ans += x
    else : ans -= x
print('possible') if ans == 0 else print('impossible')