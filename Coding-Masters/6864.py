import sys
input = sys.stdin.readline

# 1. 헥스코드 입력받기
hex_code = input().rstrip()
ans = '#'
for i in range(1, len(hex_code), 2) :
    code = hex_code[i:i+2]
    # 3. 16진수 -> 10진수로 변환
    code = int(code, 16)
    # 4. 255의 보수 적용
    code = 255 - code
    # 5. 16진수로 다시 바꿔 적용
    if len(hex(code)[2:]) == 1 :
        ans += '0' + hex(code)[2:].upper()
    else :
        ans += hex(code)[2:].upper()
print(ans)