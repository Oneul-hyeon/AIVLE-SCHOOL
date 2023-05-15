import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

def check(x) :
    count = 0
    summation = 0
    for num in array :
        if summation + num > x :
            count += 1
            summation = num
        else :
            summation += num
    count += 1
    return count

# 1. start, end 구하기
start, end = max(array), sum(array)
# 2.
while start <= end :
    # 2-1. mid 값 설정
    mid = (start+end)//2
    # 2-2. mid 값에 따라 몇 상자가 필요한지 구하기
    count = check(mid)
    # 2-3. 값이 k보다 작거나 같을 경우
    if count <= k :
        end = mid - 1
    # 2-4. 값이 k보다 클 경우
    else :
        start = mid + 1
# 3. 결과 출력
print(start)