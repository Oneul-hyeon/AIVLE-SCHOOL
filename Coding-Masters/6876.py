import sys
input = sys.stdin.readline

x, y = map(int, input().split())
if x+y >7 : ans = x+y-16
elif x+y < -8 : ans = x+y+16
else : ans = x+y
print(ans)