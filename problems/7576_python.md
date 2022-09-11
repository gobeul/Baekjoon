### 백준 7576번 - 토마토

> 2022/09/10 <br>
> 기본적인 BFS 문제였다

```python
from collections import deque

M, N = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N) ]

tomato_x = 0 # 안익은 토마토 개수
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 :
            tomato_x += 1
        elif arr[i][j] == 1:
            queue.append(((i,j,0))) # 좌표 + 날짜

while queue and tomato_x != 0:
    sti, stj, day = queue.popleft()
    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
        mi = sti + di
        mj = stj + dj

        if 0 <= mi < N and 0 <= mj < M and arr[mi][mj] == 0:
            arr[mi][mj] = 1
            queue.append((mi, mj, day+1))
            tomato_x -= 1

if tomato_x == 0:
    i, j, day = queue.pop()
    print(day) 

else:
    print(-1)
```