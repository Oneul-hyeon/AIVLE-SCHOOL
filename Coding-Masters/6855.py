import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 1. n개의 목재 정렬하기
array = sorted(list(map(int, input().split())))
# 2. start, end 값 설정
start, end = 0, n-1
while start < end :
    # 4. mid 값 설정
    mid = (start+end)//2
    # 5. 해당 인덱스의 값이 k보다 작을 경우 start + 1
    if array[mid] < k : start += 1
    # 6. 해당 인덱스의 값이 k보다 클 경우 end - 1
    elif array[mid] > k : end -= 1
    # 7. 해당 인덱스의 값이 k인 경우 값 출력 후 while 문 빠져나가기
    else :
        print(k)
        sys.exit()
print(array[start])