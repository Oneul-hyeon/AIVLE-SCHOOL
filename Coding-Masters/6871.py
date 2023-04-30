import sys
input = sys.stdin.readline

n = int(input())
# 1. 응답자의 구독료 상한선을 리스트로 입력받고 오름차순으로 정렬
array = sorted(list(map(int, input().split())))
# 2. 최대 예상 매출액 변수 설정
max_sale = -int(1e9)
for cost in array :
    # 4. 응답자의 구독료 상한선을 기준으로 예상 매출액 계산
    predict_sale = cost * n
    # 5. 최댓값 재설정
    if max_sale < predict_sale : max_sale = predict_sale
    n-=1
print(max_sale)