### 백준 7682번 - 틱택토

> 2022/11/14 <br>
> 'invalid' 조건의 규칙은 찾지 못하고 가능한 모든 경우의 수를 따져 계산했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def isRange(i, j):
    if 0 <= i < 3 and 0 <= j < 3:
        return True
    return False

def check(i, j):
    tictak = arr[i][j]
    if tictak != '.':
        for di, dj in delta:
            if isRange(i+di, j+dj) and isRange(i+di*2, j+dj*2):
                if arr[i+di][j+dj] == tictak and arr[i+di*2][j+dj*2] == tictak:
                    point[tickDict[tictak]] += 1
    else:
        point[2] += 1


def solve():
    if stoneO > stoneX: # O 가 X 보다 많은 경우
        return 'invalid'
    if stoneX - stoneO > 1: # X가 O 보다 2개 이상 많은 경우
        return 'invalid'
    if point[0] >= 1 and point[1] >= 1: # 둘다 승리 조건이 있는경우
        return 'invalid'
    if point[0] == 0 and point[1] == 0 and point[2] != 0: # 승리한 말이 없는데 빈칸이 있는경우
        return 'invalid'
    if point[0] > 0 and stoneO != stoneX: # O 가 이겼는데 둘의 말 수가 다른 경우
        return 'invalid'
    if point[1] > 0 and stoneO == stoneX: # X 가 이겼는데 둘의 말 수가 같은 경우
        return 'invalid'
    
    return 'valid'


delta = [(-1,1),(0,1), (1,1),(1,0)]

tickDict ={ # point 의 인덱스로 접근하기 위해
    'O' : 0,
    'X' : 1,
}

while 1:
    arr = list(input())
    if arr[0] == 'e':
        break
    arr = [arr[:3], arr[3:6], arr[6:9]]


    point = [0, 0, 0] # O 가 이긴 횟수, X가 이긴 횟수, 빈칸개수
    stoneCnt = {
        'O' : 0,
        'X' : 0,
        '.' : 0,
    }
    for i in range(3):
        for j in range(3):
            stoneCnt[arr[i][j]] += 1 # 각 돌의 개수 세기
            check(i, j)

    stoneO = stoneCnt['O'] # 각 돌 카운트
    stoneX = stoneCnt['X']
    
    print(solve())
```