### 백준 17070번 - 파이프 옮기기 1

> 2022/12/26 <br>
> DFS로 경우의 수를 찾았는데 python 은 시간초과 pypy 는 통과했다.<br>
> 본래의 문제 취지는 DP라고 한다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def isRange(i, j, k): # 파이프를 k방향으로 둘수 있는지?
    if k == 0:
        if 0 <= j+1 < N and not arr[i][j+1]:
            return True
    elif k == 1:
        if 0 <= i+1 < N and 0 <= j+1 < N and not arr[i][j+1] and not arr[i+1][j] and not arr[i+1][j+1]:
            return True
    elif k == 2:
        if 0 <= i+1 < N and not arr[i+1][j]:
            return True
    return False

def pipe():
    ans = 0 # 경우의수
    stack = [(0,0,0)] # 좌표 / 방향 0: 가로, 1: 대각, 2: 세로
    while stack:
        i, j, k = stack.pop()

        i += delta[k][0]
        j += delta[k][1] # 일단전진
        if (i, j) == (N-1, N-1):
            ans += 1
            continue
        for r in range(-1, 2): # -1, 0, 1
            if isRange(i, j, k+r):
                stack.append((i, j, k+r))

    return ans


delta = [(0,1), (1,1), (1,0)] # 가로, 대각, 세로
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(pipe())

```