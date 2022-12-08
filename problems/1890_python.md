### 백준 1890번 - 점프

> 2022/12/08 <br>
> 처음 문제를 봤을때는 BFS 문제인 줄 알고 풀었는데 메모리 초과가 발생했다.<br>
> DP로 접근해야되는 문제였다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque

def isRange(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False

def solve():
    ans = 0
    for i in range(N):
        for j in range(N):
            jump = arr[i][j]
            if jump == 0:
                continue
            #아래
            if isRange(i+jump, j):
                DP[i+jump][j] += DP[i][j]
            # 오른쪽
            if isRange(i, j+jump):
                DP[i][j+jump] += DP[i][j]

    print(DP[N-1][N-1])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]
DP[0][0] = 1 # 시작점은 1

solve()
```