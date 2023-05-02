import sys
from itertools import permutations

input = sys.stdin.readline

# 1. s를 리스트에 한 글자씩 입력받기
s = list(input().rstrip())
# 2. 순열을 이용하여 만들 수 있는 문자열 생성 후 중복 제거
case = list(set(permutations(s)))
# 3. 경우의 수 출력
print(len(case))
