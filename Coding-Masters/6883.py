import sys
input = sys.stdin.readline

string = input().strip()
# 1. 전체 길이 출력
print(len(string))
# 2. 공백을 제거한 길이 출력
print(len(string.replace(' ','')))
# 3. 공백을 기준으로 나눈 단어의 개수 출력
print(len(list(map(str, string.split()))))