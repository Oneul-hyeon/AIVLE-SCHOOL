import sys
input = sys.stdin.readline

# 1. 'F'를 기준으로 리스트에 문자열을 담는다.
desserts = list(map(str, input().rstrip().split('F')))
# 2. 각 문자열의 길이를 저장한다.
desserts = [len(x) for x in desserts if x]
# 3. 리스트가 빈 경우 파르페를 살 필요가 없으므로 0 출력
#    이외에는 전체 파르페 개수에서 리스트에서 가장 긴 연속된 파르페 수를 뺀 값 출력
print(0) if not desserts else print(sum(desserts) - max(desserts))