import sys
from itertools import permutations
input = sys.stdin.readline

array = [list(input().rstrip()) for _ in range(6)]
# 1. permutations를 통해 3개 단어 리스트 생성
permutations_array = permutations(range(6), 3)
ans = []
for perm in permutations_array:
    # 3. 수열을 통해 구한 단어와 나머지 단어 분리
    stand_array = [array[i] for i in perm]
    target = [array[i] for i in range(6) if i not in perm]
    # 4. 수열을 통해 구한 단어 병렬 처리
    col_array = list(zip(*stand_array))
    for col in col_array :
        # 5. 병렬 처리된 단어가 나머지 단어 리스트에 있는지 확인
        # 6. 없으면 break, 있으면 해당 문자를 나머지 단어 리스트에서 삭제
        if list(col) not in target :
            break
        else :
            target.remove(list(col))
    # 7. for문을 멀쩡히 빠져나올 경우 출력 리스트에 append
    else : ans.append(stand_array)
# 8. 출력 리스트 정렬
ans.sort()
# 9. 출력 리스트의 첫 번째 값 출력
for line in ans[0] :
    print(''.join(line))