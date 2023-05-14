import sys
input = sys.stdin.readline

numbers = list(map(int, str(input().rstrip())))
# 1. 숫자 리스트 만들기
multiply = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# 2. 초기 Y 구하기
Y = 0
for i in range(len(numbers[:-1])) :
    Y += numbers[i] * multiply[i]
# 3. 한 글자씩 수를 바꿔가면서 값이 일치하는지 count
count = 0
for i in range(len(numbers[:-1])) :
    Y -= numbers[i] * multiply[i]
    for j in range(10) :
        if j != numbers[i] :
            Y += j * multiply[i]
            if (11 - (Y % 11)) % 10 == numbers[-1] : count += 1
            Y -= j * multiply[i]
    Y += numbers[i] * multiply[i]
print(count)