import sys, time
from itertools import permutations
input = sys.stdin.readline

n = int(input())
# 1. 하나의 리스트에 문자열 입력받기
array = [input().rstrip() for _ in range(n)]
# 2. 순열 만들기
perm = permutations(array)
ans = 'NO'
for string in perm :
    # 4. 하나의 문자열로 만들어 팰린드롬 여부 확인
    string = ''.join(string)
    if string == string[::-1] :
        ans = 'YES'
        break
# 6. 결과 출력
print(ans)