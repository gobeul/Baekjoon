### 백준 14923번 - 미로탈출

> 2022/12/29 <br>
> 2206번 벽 부수고 이동하기와 같은 문제이다.<br>
> 

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque

def isRange(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    return False

def BFS(si, sj, ei, ej):
    que =  deque([(si, sj, 0, 0)]) # 좌표 / 거리 / 마법사용 여부
    visited[0][si][sj] = True

    while que:
        i, j, d, m = que.popleft()
        if (i,j) == (ei, ej):
            return d
        for di, dj in delta:
            mi, mj = i + di, j + dj
            if isRange(mi, mj):
                if not arr[mi][mj] and not visited[m][mi][mj]: # 마법안쓰고 갈 수 있는 경우
                    visited[m][mi][mj] = True
                    que.append((mi,mj,d+1,m))
                elif arr[mi][mj] and m == 0: # 마법사용
                    visited[1][mi][mj] = True
                    que.append((mi,mj,d+1,1))

    return -1


delta = [(0,1), (0,-1), (1,0), (-1,0)]
N, M = map(int, input().split())
si, sj = map(int, input().split()) # 출발좌표
ei, ej = map(int, input().split()) # 도착 좌표

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[False]*M for _ in range(N) ] for _ in range(2)] # 3차원 배열

print(BFS(si-1, sj-1, ei-1, ej-1))

```