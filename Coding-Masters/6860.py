import sys
input = sys.stdin.readline

n = int(input())
# 1
for i in range(int(n**0.5), 0, -1) :
    # 2. 픽셀의 개수 n % i == 0 이 되는 최초의 구간 찾기
    if n%i == 0 :
        # 3. 찾을 경우 a, b 출력하고 for문 탈출하기
        print(i, n//i)
        break