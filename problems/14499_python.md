### 백준 14499번 - 주사위 굴리기

> 2022/10/11 <br>
> 동서남북 으로 구를 때 숫자위치가 일정하게 변하는 것을 이용하여 해결 할 수 있었다.

```python
import sys
input = sys.stdin.readline

def move_dice(d):
    global dice

    if d == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif d == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif d == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]


def num_copy(i, j):
    if arr[i][j] != 0: # 0 이 아니면
        dice[5], arr[i][j] = arr[i][j], 0

    else:
        arr[i][j] = dice[5]
    
    print(dice[0])


delta = [(0,0), (0,1), (0,-1), (-1,0), (1,0)] # x, 동, 서, 북, 남

N, M, x, y, k = map(int, input().split())

arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

comm = list(map(int, input().split()))

dice = [0,0,0,0,0,0] 
arr[x][y], dice[5] = 0, arr[x][y] # 초기 세팅

i, j = x, y # 현재 위치
for c in comm:
    mi, mj = i+delta[c][0], j+delta[c][1]
    if 0 <= mi < N and 0 <= mj < M :
        i, j = mi, mj
        move_dice(c)
        num_copy(i, j)
```