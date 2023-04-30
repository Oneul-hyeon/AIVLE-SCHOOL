import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
# 1. 리스트 입력받기
array = list(map(int, input().split()))
# 2. Counter 함수 사용
counter = Counter(array).most_common()
counter = sorted(counter, key = lambda x : [-x[1], x[0]])
# 3. 값 출력
print(counter[0][0])