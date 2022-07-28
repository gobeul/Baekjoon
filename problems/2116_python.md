### 백준 2116번 - 주사위 쌓기

> 2022/07/27 <br>
> 창의적인 방법은 안떠올랐다.
> 첫번째 바닥면이 A,B,C,D,E,F 알 경우의 수를 모두 구해서 해결했다.
> 모든 경우의 수를 구했기에 시간초과를 걱정했었는데 시간초과가 발생하지는 않았다.

```python
def dice_sum(word, trydice_list, N):
    # word 를 받아 인덱스로 반환
    if word == "A":
        alpha_idx = 0
        revers_alpha_idx = 5
    elif word == "B":
        alpha_idx = 1
        revers_alpha_idx = 3
    elif word == "C":
        alpha_idx = 2
        revers_alpha_idx = 4
    elif word == "D":
        alpha_idx = 3
        revers_alpha_idx = 1
    elif word == "E":
        alpha_idx = 4
        revers_alpha_idx = 2
    else:
        alpha_idx = 5
        revers_alpha_idx = 0

    top_spot = trydice_list[0][revers_alpha_idx] # 윗면, 아랫면 주사위 값
    bottom_spot = trydice_list[0][alpha_idx]

# next_spot_alpha = 윗면 주사위의 알파벳(인덱스)
# bottom_spot_alpha = 아랫면 주사위의 알파벳(인덱스)

    del trydice_list[0][trydice_list[0].index(top_spot)] # 윗면 아랫면은 옆면이 될 수 없음
    del trydice_list[0][trydice_list[0].index(bottom_spot)]

    ans = max(trydice_list[0]) # 1번 주사위 놓았을때 최대값

    cnt = 1
    while cnt != N:
        # 2번째 주사위의 바닥을 1번 주사위 윗면과 맞추기 위해 1번 윗면의 숫자를 2번에서 찾아 인덱스를 반환한다. ()
        bottom_spot_alpha = trydice_list[cnt].index(top_spot) # 2번째 아랫면 주사위 알파벳 인덱스
        
        # 짝 찾기
        if bottom_spot_alpha == 0 : # A = F
            top_spot_alpha = 5
        elif bottom_spot_alpha == 1 :
            top_spot_alpha = 3
        elif bottom_spot_alpha == 2 :
            top_spot_alpha = 4
        elif bottom_spot_alpha == 3 :
            top_spot_alpha = 1
        elif bottom_spot_alpha == 4 :
            top_spot_alpha = 2
        else:
            top_spot_alpha = 0
        
        bottom_spot = top_spot # 2번 주사위 아랫면의 숫자 == 1번 주사위 윗면 숫자
        top_spot = trydice_list[cnt][top_spot_alpha]

        del trydice_list[cnt][trydice_list[cnt].index(top_spot)] # 다음 주사위 윗면 아랫면 숫자 제거
        del trydice_list[cnt][trydice_list[cnt].index(bottom_spot)]

        ans += max(trydice_list[cnt]) # 최대값 추가
        cnt += 1
    return ans



import sys
input = sys.stdin.readline
import copy

N = int(input())

try_dice = []
for i in range(N):
    a, b, c, d, e, f = map(int, input().split())

    try_dice.append([a,b,c,d,e,f])

try_dice2 = copy.deepcopy(try_dice) # 원본 보존할 리스트 생성

a = ["A", "B", "C", "D", "E", "F"]

ans = [0]*6

for i, v in enumerate(a):
    ans[i] = dice_sum(v, try_dice, N)
    try_dice = copy.deepcopy(try_dice2)

print(max(ans))
```