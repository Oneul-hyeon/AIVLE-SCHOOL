import sys
input = sys.stdin.readline

def check(i) :
    # 6. 그림 만들기
    find_array = []
    for x in range(n//i) :
        find_array.append(array[x][:m//i])

    # 7. 만들 수 있는 그림인지 확인
    for x in range(n) :
        for y in range(0, m, m//i) :
            if array[x][y:y+m//i] != find_array[x%len(find_array)] : return 0
    else : return find_array

n, m = map(int, input().split())
array = [input().rstrip() for _ in range(n)]

# 1. n, m 의 공약수를 찾아 리스트에 내림차순으로 정렬
mod = []
for i in range(min(n, m), 0, -1) :
    if n % i == 0 and m % i == 0 : mod.append(i)
# 2.for문 <- 1에서 구한 공약수 리스트
for i in mod :
    # 3. 재귀함수 실행
    result = check(i)
    if result != 0 :
        # 4. 재귀함수에서 리스트 반환 시 결과 출력 후 for문 탈출
        for line in result :
            print(line)
        break
