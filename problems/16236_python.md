### 백준 16236번 - 아기 상어

> 2022/09/04 <br>
> 기본 구조는 BFS 인데 조건이 이것저것 붙어서 까다로운 느낌이다.<br>
> 시간 초과가 꽤 많이 났던문젠데 백트래킹이 가능한 요소가 더 없을까..?<br>
> python3 기준 1876ms

```python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(fish):
    global backtracking
    
    while stack:
        si, sj, d = stack.popleft()

        if d >= backtracking:
            return
        for di, dj in delta:
            mi = di + si
            mj = dj + sj
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == False and arr[mi][mj] <= shark[2] :
                if (mi, mj) == (fish[0], fish[1]):
                    c_fish[3] = d+1
                    if backtracking > d+1:
                        backtracking = d+1
                    feed.append((fish[0], fish[1], fish[2], fish[3]))
                    return

                stack.append((mi,mj,d+1))
                visited[mi][mj] = True

delta = [(-1,0), (1,0), (0,-1), (0,1)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

fish = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9 :
            shark = [i, j, 2, 0] # 상어 좌표 / 크기 / 먹은 물고기
            arr[i][j] = 0
        elif arr[i][j] != 0 :
            fish.append((i,j,arr[i][j],9999)) # 물고기 좌표, 크기, 거리


target = [] # 크기가 작은 물고기
time = 0

while 1:
    # ggg = input()
    for i, j, size, d in fish: # 먹을 수 있는 물고기 확인
        if shark[2] > size and arr[i][j] != 0:
            target.append([i,j,size,d])
    feed = [] # 먹을 수 있는 물고기
    backtracking = 9999 # 먹을 수 있는 물고기중 최소 거리
    si, sj = shark[0], shark[1]
    for c_fish in target:
        visited = [[False]*N for _ in range(N)]
        stack = deque()
        stack.append((si, sj, 0))
        visited[si][sj] = True
        BFS(c_fish)
        if c_fish[3] == 1:
            break
    target = [] # 초기화
    feed.sort(key=lambda x : (x[3], x[0], x[1])) # 거리, 행, 열 순 정렬
    ccc += len(feed)
    for c_fish in feed:
        if c_fish[3] != 9999: # 먹을 수 있는 위치라면
            shark = [c_fish[0], c_fish[1], shark[2], shark[3]+1] # 먹음
            arr[c_fish[0]][c_fish[1]] = 0 # 빈공간으로
            time += c_fish[3]
            if shark[2] == shark[3]: # 성장 가능?
                shark[2] += 1
                shark[3] = 0
            feed = [] # 초기화
            break
    else: # 먹을 수 있는 물고기가 없다.
        print(time)
        break
```