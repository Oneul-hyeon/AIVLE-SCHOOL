import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n) :
    # 2. 두 수를 곱해 출력할 변수에 더하기
    ans += a[i] * b[i]
print(ans)