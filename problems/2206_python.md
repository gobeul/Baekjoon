### 백준 2206번 - 벽 부수고 이동하기

> 2022/09/25 <br>
> 처음에는 단순히 2차원 배열을 BFS 와 벽을 뚫을 기회를 쓴건지 아닌지를 확인 할 수 있는 변수를 하나 추가해서 돌렸는데 방문배열을 공유하면서 문제가 있었다.<br>
> 다른 분들의 코드를 참고했는데 3차원 접근하여 푸신분들이 많았고<br>
> 나도 이를 참고하여 풀이했다.<br>

> 3차원으로 벽을 뚫어을때 방문 처리 배열을 하나 더 만들어서 해결하였다.

```python
import sys
input = sys.stdin.readline
from collections import deque

def gogo():
    visited = [[[False]*M for _ in range(N)] for r in range(2)] # 3차원
    que = deque([(0,0,0,1)])
    visited[0][0][0] = True

    while que:
        w, i, j, dis = que.popleft()
        for di, dj in delta:
            mi, mj = i+di, j+dj
            if (mi, mj) == (N-1, M-1):
                return dis+1
            if 0 <= mi < N and 0 <= mj < M:
                if arr[mi][mj] == "1" and w == 0:
                    visited[1][mi][mj] = True
                    que.append((1, mi, mj,dis+1))
                elif arr[mi][mj] == "0" and not visited[w][mi][mj]:
                    visited[w][mi][mj] = True
                    que.append((w, mi, mj, dis+1))

    return -1


delta = [(0,1), (0,-1), (1,0), (-1,0)]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

if (N, M) == (1, 1):
    print(1)
    quit()

print(gogo())
```