import sys
input = sys.stdin.readline

# 4. 재귀 함수 선언
def dfs(ans) :
    # 4-1. 종료 조건 선언
    if len(ans) == k :
        print(ans)
        return
    for char in array :
        # 4-3. 재귀 함수 실행
        dfs(ans+char)

n, k = map(int, input().split())
# 1. 리스트에 알파벳 한 글자씩 입력받아 정렬하기
array = sorted(list(input().rstrip()))
# 2. 출력 문자열 선언
ans = ''
# 3. 재귀 함수 실행
dfs(ans)
