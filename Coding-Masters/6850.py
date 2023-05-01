import sys
input = sys.stdin.readline

# 1. 답안 입력받기
string = input().rstrip()
# 2. 답안의 길이 구하기
n = len(string)//2
# 3. left, right 설정
left, right = 0, 2*n - n
while left < right :
    # 4-1. 치팅 검사 후 치팅이 맞다면 결과 출력 후 프로그램 종료
    if string[left:left+n] == string[:left] + string[left+n:] or string[right:right+n] == string[:right] + string[right+n:] :
        print('YES')
        print(string[left:left+n]) if string[left:left+n] == string[:left] + string[left+n:] else print(string[right:right+n])
        sys.exit()
    # 4-2. left, right 재설정
    left+=1
    right-=1
# 5. while문을 빠져나왔다면 치팅이 아니므로 결과 출력
print('NO')