### 백준 17836번 - 공주님을 구해라!

> 2022/09/29 <br>
> 무난한 BFS 문제

```python
import sys
sys.stdin = open("eee.txt", "r")
from collections import deque
input = sys.stdin.readline

def BFS(si, sj, ei, ej): # 출빌 좌표 와 도착 좌표
    visited = [[False]*M for _ in range(N)]
    que = deque([(si, sj, 0)])
    visited[si][sj] = True
    while que:
        i, j, T = que.popleft()
        for di, dj in delta:
            mi, mj = i+di, j+dj
            if 0 <= mi < N and 0 <= mj < M and not visited[mi][mj] and arr[mi][mj] != 1:
                if (mi, mj) == (ei, ej):
                    return T+1
                visited[mi][mj] = True
                que.append((mi, mj, T+1))
    
    return 999999999 # 경로가 없을 때


delta = [(0,1), (0,-1), (1,0), (-1,0)]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            gram = (i, j) # 그람 좌표 저장

case1 = BFS(0,0,N-1,M-1) # 그람 없이 바로 가기.
case2 = BFS(0,0,gram[0], gram[1]) + (N-1-gram[0]) + (M-1-gram[1]) # 그람 먹고 가기

if case1 > K and case2 > K:
    print('Fail')
elif case1 <= K and case2 <= K:
    print(min(case1, case2))
else:
    print(min(case1, case2))
```